import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 저장 디렉토리 & 파일명 설정
SAVE_DIR = r"D:\공모전자료"
os.makedirs(SAVE_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(SAVE_DIR, "ai_edunet_data.xlsx")

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def get_total_pages():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.pagination_box")))
    pag = driver.find_element(By.CSS_SELECTOR, "div.pagination_box")
    nums = [int(a.text) for a in pag.find_elements(By.TAG_NAME, "a") if a.text.strip().isdigit()]
    return max(nums) if nums else 1

def crawl_all():
    driver.get("https://ai.edunet.net/swTchLrngData/list/409")
    total = get_total_pages()
    print(f"🔖 총 페이지 수: {total}")

    records = []

    for page in range(1, total+1):
        # 1) 페이지 클릭
        btn = driver.find_element(By.XPATH, f"//div[@class='pagination_box']//a[text()='{page}']")
        btn.click()

        # 2) 클릭 후 5초 여유 주기
        time.sleep(5)

        # 3) 콘텐츠 로드 대기
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sub_content_box ul li")))
        items = driver.find_elements(By.CSS_SELECTOR, ".sub_content_box ul li")
        print(f"➡️ [{page}/{total}] 아이템 {len(items)}개 수집 중…")

        for item in items:
            try:    cat  = item.find_element(By.CSS_SELECTOR, "div.cont_box > a dl > dt").text.strip()
            except: cat  = ""
            try:    title= item.find_element(By.CSS_SELECTOR, "div.cont_box > a dl > dd").text.strip()
            except: title= ""
            try:    date = item.find_element(By.CSS_SELECTOR, "div.cont_box > ul > li.date").text.strip()
            except: date = ""

            if not (cat or title or date): 
                continue
            records.append({"카테고리": cat, "제목": title, "날짜": date})

    driver.quit()

    df = pd.DataFrame(records)
    df.to_excel(OUTPUT_PATH, index=False)
    print(f"✅ 크롤링 완료! 저장된 파일: {OUTPUT_PATH}")

if __name__ == "__main__":
    crawl_all()
