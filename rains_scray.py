import time
import re
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

# driver = webdriver.Chrome(ChromeDriverManager().install())

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
    "//option[. = '06:　京都市内１棟']"
]


# =================================================================
# ログインページオープン
driver = webdriver.Chrome(ChromeDriverManager().install())
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




def mainpage_scrowl(select_page_one):

    # 以下メインページ=================================================================
    driver.get('https://system.reins.jp/main/BK/GBK001210')
    # 売買物件検索
    time.sleep(3)
    # 「検索条件を表示」クリック
    driver.find_element(By.CSS_SELECTOR,"span.align-middle").click()
    time.sleep(2)
    # 「保存した検索条件の選択」クリック
    dropdown = driver.find_element(By.ID, "__BVID__14")
    time.sleep(1)
    # セレクトボックス内の保存条件をクリック
    dropdown.find_element(By.XPATH, select_page_one).click()
    time.sleep(2)
    # 「読込」ボタンクリック
    driver.find_element(By.CSS_SELECTOR,
                        ".mt-3:nth-child(2) > .row:nth-child(1) > .col-sm-2 > .btn").click()
    time.sleep(2)
    # ポップアップメニュー　クリック
    driver.find_element(By.CSS_SELECTOR,
                        "#__BVID__513___BV_modal_footer_ > button").click()
    time.sleep(1)
    # 下部「検索」ボタンクリック
    driver.find_element(By.CSS_SELECTOR, "button.btn.p-button.btn-primary.btn-block.px-0").click()
    time.sleep(3)

    # ============================================================

    # csv reading
    def csv_read(filename):
        with open(filename, encoding='utf8', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                print(row)


    # ============================================================

    # 記録用要素抽出

    # 検索ページ項目
    pagename = select_page_one.split(':')[-1].replace("']","")

    # 新着データ取得
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    # 物件番号
    bukken_nums = soup.select(
        '#__BVID__545 > div > div.p-table.small > div.p-table-body > div > div:nth-child(4)')
    # 物件種目
    bukken_object_typies = soup.select('#__BVID__545 > div > div.p-table.small > div.p-table-body > div > div:nth-child(5)')
    # 価格
    bukken_plicies = soup.select('#__BVID__545 > div > div.p-table.small > div.p-table-body > div > div.p-table-body-item.font-weight-bold')


    for i, num in enumerate(bukken_nums):
        # 物件データとしてまとめる
        bukken_data = [num.text, pagename.replace("\u3000",""),
                       bukken_object_typies[i].text, bukken_plicies[i].text]

        print(bukken_data)

        with open('new_data.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(bukken_data)


    # # ファイルの扱い　ファイルがあると記録されないのを修正すること
    # if os.path.isfile('last_data.csv'):
    #     print('記録呼出・表示')
    #     with open('last_data.csv', encoding='utf8', newline='') as f:
    #         csvreader = csv.reader(f)
    #         for row in csvreader:
    #             print(row)
    # else:
    #     print('新規記録保存中')
    #     for bukken_data in bukken_datas_new:
    #         with open('last_data.csv', 'a', newline='') as f:
    #             writer = csv.writer(f)
    #             writer.writerow(bukken_data)



    # # ドロップダウン検索ページへ「戻る」アイコンクリック


if __name__ == '__main__':

    for name in selects_dropdown:
        mainpage_scrowl(name)
    driver.close()

    # テスト用
    # name = "//option[. = '01:　三重四日市　外全']"
    # mainpage_scrowl(name)


