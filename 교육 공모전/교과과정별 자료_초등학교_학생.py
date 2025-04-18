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
wait   = WebDriverWait(driver, 5)      # 요소 로딩 최대 5초 대기

def click_filter(tab_name):
    """‘전체’ 대신 교사/학생 탭 클릭 후 로딩 대기"""
    try:
        btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//ul[contains(@class,'filter_tab_number')]//li[normalize-space(text())='{tab_name}']")
        ))
        btn.click()
        # 필터 적용 후 첫 info_box 하나 뜰 때까지 대기
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.info_box")))
    except Exception:
        print(f"⚠️ 필터 ‘{tab_name}’ 클릭 실패")

def get_total_pages():
    """현재 필터 상태에서 총 페이지 수 구하기"""
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.pagination_box")))
    # 마지막 그룹으로 이동
    try:
        driver.find_element(By.CSS_SELECTOR, "div.pagination_box a.btn_last").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.pagination_box a.current_page")))
    except NoSuchElementException:
        pass
    pag = driver.find_element(By.CSS_SELECTOR, "div.pagination_box")
    nums = [int(a.text) for a in pag.find_elements(By.TAG_NAME, "a") if a.text.strip().isdigit()]
    total = max(nums) if nums else 1
    # 첫 페이지로 복귀
    try:
        driver.find_element(By.CSS_SELECTOR, "div.pagination_box a.btn_first").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.pagination_box a.current_page")))
    except NoSuchElementException:
        pass
    return total

def crawl_for(tab_name, records):
    """주어진 탭(교사/학생) 아래 전체 페이지 크롤링"""
    driver.get(URL)
    click_filter(tab_name)
    total_pages = get_total_pages()
    print(f"🔖 [{tab_name}] 전체 {total_pages}페이지 크롤링 시작")

    current = 1
    while current <= total_pages:
        # pagination 로드 대기
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.pagination_box")))
        pag = driver.find_element(By.CSS_SELECTOR, "div.pagination_box")
        # 숫자 링크만 필터 & 정렬
        links = sorted(
            [(int(a.text), a) for a in pag.find_elements(By.TAG_NAME, "a")
             if a.text.strip().isdigit()],
            key=lambda x: x[0]
        )
        for page_num, link in links:
            if page_num < current or page_num > total_pages:
                continue
            try:
                link.click()
            except:
                print(f"⚠️ [{tab_name} {page_num}] 클릭 실패, 스킵")
                current = page_num + 1
                continue

            # info_box 등장 대기
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.info_box")))
            except TimeoutException:
                print(f"⚠️ [{tab_name} {page_num}] 로딩 타임아웃, 스킵")
                current = page_num + 1
                continue

            print(f"➡️ [{tab_name} {page_num}/{total_pages}] 수집 중…")
            for box in driver.find_elements(By.CSS_SELECTOR, "div.info_box"):
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
                if title or date:
                    records.append({
                        "대상": tab_name,
                        "책제목": title,
                        "날짜": date
                    })
            current = page_num + 1

        # 다음 그룹으로 넘어가기
        if current <= total_pages:
            try:
                prev = pag.find_element(By.CSS_SELECTOR, "a.current_page").text.strip()
                driver.find_element(By.CSS_SELECTOR, "div.pagination_box a.btn_next").click()
                time.sleep(3)
                # 다음 그룹 첫 페이지 번호 확인
                wait.until(EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, "div.pagination_box a.current_page"),
                    str(int(prev) + len(links))
                ))
            except:
                print(f"⚠️ [{tab_name}] 다음 그룹 전환 실패, 종료")
                break

def main():
    records = []
    for tab in ["교사", "학생"]:
        crawl_for(tab, records)
    driver.quit()

    df = pd.DataFrame(records, columns=["대상", "책제목", "날짜"])
    df.to_excel(OUTPUT_XLS, index=False)
    print(f"✅ 크롤링 완료! 저장 경로: {OUTPUT_XLS}")

if __name__ == "__main__":
    main()
