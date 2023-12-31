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



class TestTC01():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(5) # Implicitly await for 10s
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_purchase_without_login(self):
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

    # Step 4 -----------------------------
    # Arrange and assert for Step 4
    self.driver.find_element(By.ID, "cartur").click()

    assert self.driver.current_url == "https://www.demoblaze.com/cart.html"
    time.sleep(3)

    # Step 5 -----------------------------
    # Arrange and assert for Step 5
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

    modal = self.driver.find_element(By.CSS_SELECTOR, ".modal-content")
    assert modal is not None

    # Arrange: Setting all the form inputs
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Javier")
    self.driver.find_element(By.ID, "country").click()
    self.driver.find_element(By.ID, "country").send_keys("Argentina")
    self.driver.find_element(By.ID, "city").send_keys("Rincón de Milberg")
    self.driver.find_element(By.ID, "card").click()
    self.driver.find_element(By.ID, "card").send_keys("1253468524")
    self.driver.find_element(By.ID, "month").click()
    self.driver.find_element(By.ID, "month").send_keys("01")
    self.driver.find_element(By.ID, "year").click()
    self.driver.find_element(By.ID, "year").send_keys("25")


    # Step 5 -----------------------------
    # Arrange and assert for Step 5
    self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
    self.driver.implicitly_wait(5)

    modal = self.driver.find_element(By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible")
    assert modal is not None



    element = self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
