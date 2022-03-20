
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(ChromeDriverManager().install())


# RAINS アカウント情報 ==============================================

rains_id = '125100372700' # ID
rains_passwd = 'cosei0304' # Password
# ログインページURL
rains_top_url = "https://system.reins.jp/login/main/KG/GKG001200"
# =================================================================


# ログインページオープン
driver.get(rains_top_url)
time.sleep(3)
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
driver.find_element(By.CSS_SELECTOR,
                         ".b-custom-control-lg > .custom-control-label").click()


time.sleep(3)
