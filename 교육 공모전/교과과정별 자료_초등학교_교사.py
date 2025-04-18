import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ─── 설정 ───────────────────────────────────────
SAVE_DIR   = r"D:\공모전자료"
FILENAME   = "에듀넷_교과과정별자료_초등학교.xlsx"
OUTPUT_XLS = os.path.join(SAVE_DIR, FILENAME)
URL        = "https://ai.edunet.net/sbjSrcData/list/398"

os.makedirs(SAVE_DIR, exist_ok=True)

driver = webdriver.Chrome()
wait   = WebDriverWait(driver, 5)  # 최대 5초 대기

def get_total_pages():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.pagination_box")))
    try:
        driver.find_element(By.CSS_SELECTOR, "div.pagination_box a.btn_last").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.pagination_box a.current_page")))
    except NoSuchElementException:
        pass

    pag = driver.find_element(By.CSS_SELECTOR, "div.pagination_box")
    nums = [int(a.text) for a in pag.find_elements(By.TAG_NAME, "a") if a.text.strip().isdigit()]
    total = max(nums) if nums else 1

    try:
        driver.find_element(By.CSS_SELECTOR, "div.pagination_box a.btn_first").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.pagination_box a.current_page")))
    except NoSuchElementException:
        pass

    return total

def crawl_all():
    driver.get(URL)
    total_pages = get_total_pages()
    print(f"🔖 전체 {total_pages}페이지 크롤링 시작")

    records = []
    current_page = 1

    while current_page <= total_pages:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.pagination_box")))
        pag = driver.find_element(By.CSS_SELECTOR, "div.pagination_box")
        num_links = sorted(
            [(int(a.text), a) for a in pag.find_elements(By.TAG_NAME, "a") if a.text.strip().isdigit()],
            key=lambda x: x[0]
        )

        for page_num, link in num_links:
            if page_num < current_page or page_num > total_pages:
                continue
            try:
                link.click()
            except:
                print(f"⚠️ [{page_num}] 클릭 실패, 건너뜁니다.")
                current_page = page_num + 1
                continue

            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.info_box")))
            except TimeoutException:
                print(f"⚠️ [{page_num}] 로딩 타임아웃(5초), 스킵합니다.")
                current_page = page_num + 1
                continue

            print(f"➡️ [{page_num}/{total_pages}] 수집 중…")
            info_boxes = driver.find_elements(By.CSS_SELECTOR, "div.info_box")
            for box in info_boxes:
                try:
                    title = box.find_element(By.CSS_SELECTOR, "p.title").text.strip()
                except:
                    title = ""
                try:
                    date = box.find_element(
                        By.CSS_SELECTOR,
                        "ul.option_box.date > li:nth-child(1) > strong"
                    ).text.strip()
                except:
                    date = ""
                # 여기에 '교사' 컬럼을 추가
                if title or date:
                    records.append({
                        "교사": "교사",
                        "책제목": title,
                        "날짜": date
                    })

            current_page = page_num + 1

        if current_page <= total_pages:
            try:
                prev_page = int(pag.find_element(By.CSS_SELECTOR, "a.current_page").text.strip())
            except:
                prev_page = None
            try:
                driver.find_element(By.CSS_SELECTOR, "div.pagination_box a.btn_next").click()
                time.sleep(3)
                if prev_page is not None:
                    expected = prev_page + len(num_links)
                    wait.until(EC.text_to_be_present_in_element(
                        (By.CSS_SELECTOR, "div.pagination_box a.current_page"),
                        str(expected)
                    ))
            except:
                print("⚠️ 다음 그룹 전환 대기 실패, 이어서 진행합니다.")

    driver.quit()

    # DataFrame 생성 시 컬럼 순서 지정
    df = pd.DataFrame(records, columns=["교사", "책제목", "날짜"])
    df.to_excel(OUTPUT_XLS, index=False)
    print(f"✅ 크롤링 완료! 파일 저장: {OUTPUT_XLS}")

if __name__ == "__main__":
    crawl_all()
