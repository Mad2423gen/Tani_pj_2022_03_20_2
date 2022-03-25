
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC



# RAINS アカウント情報 ==============================================

rains_id = '125100372700' # ID
rains_passwd = 'cosei0304' # Password

# ログインページURL
rains_top_url = "https://system.reins.jp/login/main/KG/GKG001200"

# 検索項目（ドロップダウンバリュー）
page1 = "//option[. = '01:　三重四日市　外全']"
page2 = "//option[. = '02:　滋賀１棟']"
page3 = "//option[. = '03:　三重県桑名市']"
page4 = "//option[. = '04:　滋賀県戸建て']"
page5 = "//option[. = '05:　滋賀土地']"
page6 = "//option[. = '06:　京都市内１棟']"
selects_dropdown = [page1, page2, page3, page4, page5, page6]

# =================================================================

def mainpagescray(url,values):
    driver = webdriver.Chrome(ChromeDriverManager().install())
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

    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # ログインボタン
    time.sleep(5)
    # 売買物件検索
    driver.find_element(By.CSS_SELECTOR,
                        ".card:nth-child(2) .row:nth-child(3) > .pr-2 > .btn").click()
    time.sleep(5)
    # 「検索条件を表示」クリック
    driver.find_element(By.CSS_SELECTOR,
                        ".card:nth-child(3) .align-middle:nth-child(1)").click()
    time.sleep(2)
    # 「保存した検索条件の選択」クリック
    dropdown = driver.find_element(By.ID, "__BVID__102")
    time.sleep(1)
    # セレクトボックス内の保存条件をクリック
    dropdown.find_element(By.XPATH, "//option[. = '01:　三重四日市　外全']").click()
    time.sleep(1)

    element = driver.find_element(By.ID, "__BVID__102")
    time.sleep(1)

    actions = ActionChains(driver)
    time.sleep(1)

    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.ID, "__BVID__102")
    actions = ActionChains(driver)
    time.sleep(1)

    actions.move_to_element(element).release().perform()
    time.sleep(2)
    # 「読込」ボタンクリック
    driver.find_element(By.CSS_SELECTOR,
                        ".mt-3:nth-child(2) > .row:nth-child(1) > .col-sm-2 > .btn").click()
    time.sleep(2)
    # ポップアップメニュー　クリック
    driver.find_element(By.CSS_SELECTOR,
                        "#\\__BVID__601___BV_modal_footer_ > .btn").click()
    time.sleep(2)
    # 下部「検索」ボタンクリック
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    time.sleep(5)


    # 抽出処理=====================================================
    # 件名のみ読み込み（物件番号で識別）
    bukken_nums = driver.find_elements\
        (By.CSS_SELECTOR, "div.p-table-body-item")
    # 件名保存
    # ファイル名整形
    filename = "data/{}.txt".format(values.split(':')[1].replace("']", ""))
    # ファイル保存
    for name in bukken_nums:
        with open(filename, 'w', encoding='utf-8')as f:
            f.write(name.text)
    # ============================================================

    # 「戻る」アイコンクリック
    driver.find_element(By.CSS_SELECTOR, "button.p-frame-backer").click()

    time.sleep(10)


if __name__ == '__main__':

    # mainpagescray(rains_top_url,selects_dropdown)
    # driver.close()










