import time
import datetime
import difflib
import re
import os
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
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
    "//option[. = '06:　京都市内１棟']"
]
# =================================================================
# ログインページ用
def scrowd_login():
    driver.get(rains_top_url)
    time.sleep(5)
    # ID入力
    driver.find_element(By.ID, "__BVID__13").click()
    time.sleep(0.3)
    driver.find_element(By.ID, "__BVID__13").send_keys(rains_id)
    time.sleep(0.3)
    # PASSWORD入力
    driver.find_element(By.ID, "__BVID__16").click()
    time.sleep(0.3)
    driver.find_element(By.ID, "__BVID__16").send_keys(rains_passwd)
    time.sleep(0.3)
    # 「ガイドラインを尊守します」チェックボックスクリック
    driver.find_element(By.CSS_SELECTOR,
                        ".b-custom-control-lg > .custom-control-label").click()
    time.sleep(0.3)
    # ログインボタン
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(5)

# =================================================================
# 本ページ処理用
def mainpage_scrowl(select_page_one):
    # 以下メインページ=================================================================
    driver.get('https://system.reins.jp/main/BK/GBK001210')
    # 売買物件検索
    time.sleep(4)
    # 「検索条件を表示」クリック
    driver.find_element(By.CSS_SELECTOR,"span.align-middle").click()
    time.sleep(0.2)
    # 「保存した検索条件の選択」クリック
    dropdown = driver.find_element(By.ID, "__BVID__14")
    time.sleep(0.2)
    # セレクトボックス内の保存条件をクリック
    dropdown.find_element(By.XPATH, select_page_one).click()
    time.sleep(0.1)
    # 「読込」ボタンクリック
    driver.find_element(By.CSS_SELECTOR,
                        ".mt-3:nth-child(2) > .row:nth-child(1) > .col-sm-2 > .btn").click()
    time.sleep(1.5)
    # ポップアップメニュー　クリック
    driver.find_element(By.CSS_SELECTOR,
                        "#__BVID__513___BV_modal_footer_ > button").click()
    time.sleep(0.5)
    # 下部「検索」ボタンクリック
    driver.find_element(By.CSS_SELECTOR, "button.btn.p-button.btn-primary.btn-block.px-0").click()
    time.sleep(3)

    # ============================================================

    # csv reading
    # def csv_read(filename):
    #     with open(filename, encoding='utf8', newline='') as f:
    #         csvreader = csv.reader(f)
    #         for row in csvreader:
    #             print(row)


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
    bukken_object_typies = soup.select('#__BVID__545 > div > div.p-table.small > div.p-table-body '
                                       '> div > div:nth-child(5)')
    # 価格
    bukken_plicies = soup.select('#__BVID__545 > div > div.p-table.small > div.p-table-body > div '
                                 '> div.p-table-body-item.font-weight-bold')


    for i, num in enumerate(bukken_nums):
        # 物件データとしてまとめる
        bukken_data = [num.text, pagename.replace("\u3000",""),
                       bukken_object_typies[i].text, bukken_plicies[i].text]
        # 物件データをCSVへ記録
        with open('new_data.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(bukken_data)


# =================================================================
# ファイルの増減を抽出
def sabun_select(new, last):
    # ファイル差分抽出
    file1 = open(last) #  前回のリスト
    file2 = open(new) # 今回のリスト
    diff = difflib.Differ()
    output_diff = diff.compare(file1.readlines(), file2.readlines())

    # 差分の結果を抽出
    to_message = []
    for data in output_diff:
        # リストの増分のみ抽出
        if data[0:1] in ['+']:
            # print(data.replace('+', '').replace('"', ''))
            to_message.append(data.replace('+', '').replace('"', '').replace('\n', ''))

    file1.close()
    file2.close()

    # return to_message
    print(to_message)


# テスト用
#
# if __name__ == '__main__':
#     file_new = 'new_data.csv'
#     file_last = 'last_data.csv'
#     # messageの返り値はリスト
#     message = sabun_select(file_new,file_last)
#
#     print(message)

# =================================================================

def rains_function():
    dt = datetime.datetime.today()
    print('只今の時間：{}時'.format(dt.hour))
    if 7 <= int(dt.hour) <= 23:
        # 前回のファイルを旧ファイルに変更
        os.rename('new_data.csv', 'last_data.csv')
        # ログインページオープン
        scrowd_login()
        # 本ページ処理
        for name in selects_dropdown:
            print('RAINS・カテゴリ『{}』開始'
                  .format(name.split(':')[-1].replace("']", "")
                          .replace(' ', '')))
            mainpage_scrowl(name)
        driver.close()

        file_new = 'new_data.csv'
        file_last = 'last_data.csv'
        # 差分抽出
        to_message = sabun_select(file_new, file_last)

        # 今回のファイルを旧ファイルに変更
        os.remove('last_data.csv')

        return to_message

    # サイト時間外についての処理
    else:
        print('WEB受付時間外により処理をスキップ')
        pass



if __name__=='__main__':
    rains_function()











