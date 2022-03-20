
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(chrome_driver_path)

# RAINS アカウント情報 ==============================================

rains_id = '125100372700' # ID
rains_passwd = 'cosei0304' # Password
# ログインページURL
raint_top_url = "https://system.reins.jp/login/main/KG/GKG001200"
# =================================================================


# ログインページオープン
driver.get(raint_top_url)
time.sleep(2.5)
# ID入力
driver.find_element(By.ID, "__BVID__13").click()
time.sleep(1)
driver.find_element(By.ID, "__BVID__13").send_keys(rains_id)
# PASSWORD入力




time.sleep(3)
