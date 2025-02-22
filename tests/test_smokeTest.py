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

class TestSmokeTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_homepage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1200, 720)
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".header-today > p").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > h4")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > .centered-image")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us!")
    assert len(elements) > 0
  
  def test_adminpage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1200, 720)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".myinput:nth-child(2)")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").send_keys("john")
    self.driver.find_element(By.ID, "password").send_keys("asdd312")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".errorMessage"), "Invalid username and password."))
  
  def test_directorypage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1200, 720)
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    self.driver.find_element(By.ID, "directory-grid").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
  
  def test_joinpage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1200, 720)
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".myinput:nth-child(2)")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("John")
    self.driver.find_element(By.NAME, "lname").send_keys("Doe")
    self.driver.find_element(By.NAME, "bizname").send_keys("Buzy")
    self.driver.find_element(By.NAME, "biztitle").send_keys("Manager")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".myinput:nth-child(2)")
    assert len(elements) > 0
  
