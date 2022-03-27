# =============================================================================

#     　　　　　　　　　　　メインページ保存用スクリプト

# =============================================================================


import time
import lxml
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())

# RAINS アカウント情報 ==============================================

rains_id = '125100372700'  # ID
rains_passwd = 'cosei0304'  # Password

# ログインページURL
rains_top_url = "https://system.reins.jp/login/main/KG/GKG001200"

# 検索項目（ドロップダウンバリュー）
selects_dropdown = [
    "//option[. = '01:　三重四日市　外全']",
    "//option[. = '02:　滋賀１棟']",
    "//option[. = '03:　三重県桑名市']",
    "//option[. = '04:　滋賀県戸建て']",
    "//option[. = '05:　滋賀土地']",
    "//option[. = '06:　京都市内１棟']"]
# =================================================================

# ログインページオープン
driver.get(rains_top_url)
time.sleep(5)
# ID入力
driver.find_element(By.ID, "__BVID__13").click()
time.sleep(0.5)
driver.find_element(By.ID, "__BVID__13").send_keys(rains_id)
time.sleep(1)
# PASSWORD入力
driver.find_element(By.ID, "__BVID__16").click()
time.sleep(0.5)
driver.find_element(By.ID, "__BVID__16").send_keys(rains_passwd)
time.sleep(1)
# 「ガイドラインを尊守します」チェックボックスクリック
driver.find_element(By.CSS_SELECTOR,
                    ".b-custom-control-lg > .custom-control-label").click()
time.sleep(0.5)
# ログインボタン
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(5)




# 売買物件検索
driver.find_element(By.CSS_SELECTOR,
                    ".card:nth-child(2) .row:nth-child(3) > .pr-2 > .btn").click()
time.sleep(5)
# 「検索条件を表示」クリック
driver.find_element(By.CSS_SELECTOR,
                    ".card:nth-child(3) .p-collapse-icon").click()
time.sleep(2)
# 「保存した検索条件の選択」クリック
dropdown = driver.find_element(By.ID, "__BVID__103")
time.sleep(1)
# セレクトボックス内の保存条件をクリック
dropdown.find_element(By.XPATH, "//option[. = '01:　三重四日市　外全']").click()
time.sleep(1)

element = driver.find_element(By.ID, "__BVID__103")
# time.sleep(1)

actions = ActionChains(driver)
# time.sleep(1)

actions.move_to_element(element).click_and_hold().perform()
element = driver.find_element(By.ID, "__BVID__103")
actions = ActionChains(driver)
# time.sleep(1)

actions.move_to_element(element).release().perform()
time.sleep(2)
# 「読込」ボタンクリック
driver.find_element(By.CSS_SELECTOR,
                    ".mt-3:nth-child(2) > .row:nth-child(1) > .col-sm-2 > .btn").click()
time.sleep(2)
# ポップアップメニュー　クリック
driver.find_element(By.CSS_SELECTOR,
                    "#\\__BVID__602___BV_modal_footer_ > .btn").click()
time.sleep(2)
# 下部「検索」ボタンクリック
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
time.sleep(10)

html = driver.page_source
time.sleep(5)

# soup = BeautifulSoup(html,'lxml')

with open("page_source.txt",'w',encoding='utf-8') as sc:
    sc.write(html)



time.sleep(5)
driver.close()