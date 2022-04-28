from setup import WebDriverSetup
from pages import RegisterPage
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
username='tentestthunghie'
password='tentestthunghi123123e'

class TestRegister(WebDriverSetup):

  def test_3_register(self):
    self.driver.get('https://nroblue.com/dang-ky')
    register_page = RegisterPage(self.driver)
    sleep(1)
    register_page.register(username, password)
    sleep(2)
    register_page.submit_register()
    sleep(2)

if __name__ == '__main__':
  unittest.main()
