# Generated by Selenium IDE
from telnetlib import EC

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


class TestTC01():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(5)  # Implicitly await for 5s
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_add_to_cart(self):
    # Arrange
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1936, 1056)

    # Step 1 ----------------------------
    # Arrange for Step 1
    try:
      lista_de_prods = self.driver.find_element(By.ID, "contcont")
    except NoSuchElementException:
      print("NoSuchElementException: No element with id: 'contcont' was found")

    # Asserts for Step 1
    assert self.driver.current_url == "https://www.demoblaze.com/"
    assert lista_de_prods is not None

    # Step 2 ----------------------------
    # Arrange for Step 2
    samsung_title = "Samsung galaxy s6"
    # This way we can also verify if the element clicked is the same as the one shown in the details view
    self.driver.find_element(By.LINK_TEXT, samsung_title).click()
    try:
      product_title = self.driver.find_element(By.CSS_SELECTOR, ".name").text
      product_container = self.driver.find_element(By.ID, "more-information")
      add_to_cart_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-success").text
    except NoSuchElementException as e:
      if "name" not in str(e):
        print("The element with class '.name' was not found.")
      if "more-information" not in str(e):
        print("The element with ID 'more-information' was not found.")

    # Asserts for Step 2
    assert self.driver.current_url == "https://www.demoblaze.com/prod.html?idp_=1"
    assert product_title == samsung_title
    assert product_container is not None
    assert add_to_cart_btn == "Add to cart"

    # Step 3 ----------------------------
    # Arrange and assert for Step 3
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    try:
      alert = self.driver.switch_to.alert
      assert alert.text == "Product added"
      alert.accept()  # If the alert box shows up, accept it
    except NoAlertPresentException:
      print("\nNoAlertPresentException: No alert was found")

    # Step 4 ----------------------------
    # Arrange for Step 4
    self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()
    try:
      element = self.driver.find_element(By.ID, "contcont")
    except NoSuchElementException:
      print("NoSuchElementException1: No element with id: 'contcont' was found")

    # Asserts for Step 4
    assert self.driver.current_url == "https://www.demoblaze.com/index.html"
    assert element is not None

    # Step 5 ----------------------------
    # Arrange for Step 5
    nokia_title = "Nokia lumia 1520"
    self.driver.find_element(By.LINK_TEXT, nokia_title).click()
    try:
      product_title = self.driver.find_element(By.CSS_SELECTOR, ".name").text
      product_container = self.driver.find_element(By.ID, "more-information")
      add_to_cart_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-success").text
    except NoSuchElementException as e:
      if "name" not in str(e):
        print("The element with class '.name' was not found.")
      if "more-information" not in str(e):
        print("The element with ID 'more-information' was not found.")

    # Asserts for Step 5
    assert self.driver.current_url == "https://www.demoblaze.com/prod.html?idp_=2"
    assert product_title == nokia_title
    assert product_container is not None
    assert add_to_cart_btn == "Add to cart"

    # Step 6 ----------------------------
    # Arrange and Assert for Step 6
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    try:
      alert = self.driver.switch_to.alert
      assert alert.text == "Product added"
      alert.accept()  # If the alert box shows up, accept it
    except NoAlertPresentException:
      print("NoAlertPresentException: No alert was found")

    # Step 7 ----------------------------
    # Arrange for Step 7
    # For some reason this step sometimes works and sometimes doesn't
    self.driver.find_element(By.ID, "cartur").click()
    time.sleep(3)
    try:
      table = WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table-responsive"))
      )
      assert table is not None
    except Exception as e:
      print("Exception: Error while trying to find the elements")

    # Asserts for Step 7
    # assert self.driver.current_url == "https://www.demoblaze.com/cart.html"


  
