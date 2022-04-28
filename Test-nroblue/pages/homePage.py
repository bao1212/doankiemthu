class HomePage():

  def __init__(self, driver):
    self.driver = driver

    self.login_btn = driver.find_element_by_xpath('//a[text()=" ĐĂNG NHẬP"]')
    self.register_btn = driver.find_element_by_xpath('//a[text()=" ĐĂNG KÝ"]')
    self.forum_btn = driver.find_element_by_xpath('//a[text()="Diễn đàn"]')
    self.feedback_btn = driver.find_element_by_xpath('//a[text()="Góp ý"]')
    self.error_btn = driver.find_element_by_xpath('//a[text()="Báo lỗi"]')

  def login_page(self):
    self.login_btn.click()

  def register_page(self):
    self.register_btn.click()

  def forum(self):
    self.forum_btn.click()

  def feedback(self):
    self.feedback_btn.click()

  def error(self):
    self.error_btn.click()

  def get_feedback_btn(self):
    return self.error_btn
