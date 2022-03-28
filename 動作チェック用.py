# ==============================================================================

#                    　RAINS 動作チェック用ファイル

# ==============================================================================

import time
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

# rains_id = '125100372700'  # ID
# rains_passwd = 'cosei0304'  # Password

# ログインページURL
# rains_top_url = "https://system.reins.jp/login/main/KG/GKG001200"

# 検索項目（ドロップダウンバリュー）
selects_dropdown = [
    "//option[. = '01:　三重四日市　外全']",
    "//option[. = '02:　滋賀１棟']",
    "//option[. = '03:　三重県桑名市']",
    "//option[. = '04:　滋賀県戸建て']",
    "//option[. = '05:　滋賀土地']",
    "//option[. = '06:　京都市内１棟']"]

for name in selects_dropdown:
    print("変更前：{}".format(name))
    print('変更後：{}'.format(name.split(":")[-1]))












