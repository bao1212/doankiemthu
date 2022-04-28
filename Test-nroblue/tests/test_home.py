from pages.homePage import HomePage
import unittest

from setup import WebDriverSetup
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestHome(WebDriverSetup):

  def test_1_view_home(self):
    self.driver.get('https://nroblue.com')
    home_page = HomePage(self.driver)
    sleep(1)

    # Feed back page
    home_page.feedback()
    sleep(2)

    self.driver.find_element_by_css_selector('.color-main2 div.box-stt:first-child a').click()
    sleep(2)

    self.driver.find_element_by_xpath('//a[text()=" Quay lại"]').click()
    sleep(2)


    # Error Page
    self.driver.find_element_by_xpath('//a[text()="Báo lỗi"]').click()
    sleep(2)

    # Forum page
    self.driver.find_element_by_xpath('//a[text()="Diễn đàn"]').click()
    sleep(2)

    self.driver.find_element_by_css_selector('.color-main2 div.box-stt:first-child a').click()
    sleep(2)

    self.driver.find_element_by_xpath('//a[text()=" Quay lại"]').click()
    sleep(1)

if __name__ == '__main__':
  unittest.main()
