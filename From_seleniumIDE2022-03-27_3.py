# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test3(self):
    self.driver.get("https://system.reins.jp/login/main/KG/GKG001200")
    self.driver.set_window_size(1366, 740)
    self.driver.find_element(By.ID, "__BVID__13").click()
    self.driver.find_element(By.ID, "__BVID__13").send_keys("125100372700")
    self.driver.find_element(By.ID, "__BVID__16").click()
    self.driver.find_element(By.ID, "__BVID__16").send_keys("cosei0304")
    self.driver.find_element(By.CSS_SELECTOR, ".col > .p-checkbox .custom-control-label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".b-custom-control-lg > .custom-control-label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(2) .row:nth-child(3) > .pr-2 > .btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(3) .p-collapse-icon").click()
    dropdown = self.driver.find_element(By.ID, "__BVID__103")
    dropdown.find_element(By.XPATH, "//option[. = '01:　三重四日市　外全']").click()
    element = self.driver.find_element(By.ID, "__BVID__103")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "__BVID__103")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "__BVID__103")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".mt-3:nth-child(2) > .row:nth-child(1) > .col-sm-2 > .btn").click()
    self.driver.find_element(By.CSS_SELECTOR, "#\\__BVID__602___BV_modal_footer_ > .btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
  
