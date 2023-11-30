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

# Exceptions
from selenium.common import NoAlertPresentException, NoSuchElementException, WebDriverException


class TestTC05():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(5)  # Implicitly await for 10s
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_categories_filter(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1936, 1066)

    # Step 1 ----------------------------
    # Arrange for Step 1
    try:
      lista_de_prods = self.driver.find_element(By.ID, "contcont")
    except NoSuchElementException:
      print("NoSuchElementException1: No element with id: 'contcont' was found")

    # Asserts for Step 1
    assert self.driver.current_url == "https://www.demoblaze.com/"
    assert lista_de_prods is not None

    # Step 2 ----------------------------
    self.driver.find_element(By.ID, "itemc").click()

    samsung_title = "Samsung galaxy s6"
    phones = self.driver.find_element(By.LINK_TEXT, samsung_title)

    assert phones is not None

    # Step 3 ----------------------------
    self.driver.find_element(By.LINK_TEXT, "Laptops").click()

    laptop_title = "Sony vaio i5"
    laptops = self.driver.find_element(By.LINK_TEXT, laptop_title)

    assert laptops is not None

    # Step 4 ----------------------------
    self.driver.find_element(By.LINK_TEXT, "Monitors").click()

    monitor_title = "Apple monitor 24"
    monitors = self.driver.find_element(By.LINK_TEXT, monitor_title)

    assert monitors is not None

  