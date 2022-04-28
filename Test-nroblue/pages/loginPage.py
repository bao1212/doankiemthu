from time import sleep

class LoginPage():
  def __init__(self, driver):
    self.driver = driver

    self.username = driver.find_element_by_xpath('//input[@id="user"]')
    self.password = driver.find_element_by_xpath('//input[@id="pass"]')
    self.submit = driver.find_element_by_css_selector('.btn.color-main.font-weight-bold.form-control')

  def login(self, username, password):
    self.username.send_keys(username)
    self.password.send_keys(password)

  def submit_form(self):
    self.submit.click()
