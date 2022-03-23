
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,
                         ".card:nth-child(2) .row:nth-child(3) > .pr-2 > .btn").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,
                         ".card:nth-child(3) .align-middle:nth-child(1)").click()
time.sleep(3)
dropdown = driver.find_element(By.ID, "__BVID__102")
time.sleep(1)
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
driver.find_element(By.CSS_SELECTOR,
                         ".mt-3:nth-child(2) > .row:nth-child(1) > .col-sm-2 > .btn").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,
                         "#\\__BVID__601___BV_modal_footer_ > .btn").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

time.sleep(10)
