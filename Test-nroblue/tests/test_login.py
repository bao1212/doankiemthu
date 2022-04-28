from setup import WebDriverSetup
from pages import LoginPage
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username='kepkhu996'
password='bao12122001'

class TestLogin(WebDriverSetup):

  def test_1_login_error(self):
    self.driver.get('https://nroblue.com/dang-nhap')
    login_page = LoginPage(self.driver)
    login_page.login(username, 'password')
    sleep(1)
    login_page.submit_form()
    sleep(2)

    message = 'Thông tin đăng nhập không chính xác.'
    error_message= self.driver.find_element_by_css_selector('#notify').text
    self.assertEquals(message, error_message)


  def test_2_login_success(self):
    self.driver.get('https://nroblue.com/dang-nhap')
    login_page = LoginPage(self.driver)
    login_page.login(username, password)
    sleep(1)
    login_page.submit_form()
    sleep(2)

if __name__ == '__main__':
  unittest.main()
