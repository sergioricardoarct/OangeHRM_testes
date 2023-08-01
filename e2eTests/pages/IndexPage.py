from selenium.webdriver.common.by import By
from e2eTests.locators import LocatorsIndex
from e2eTests.pages.PageObject import PageObject


class pageIndex(PageObject):
    base_url = 'https://opensource-demo.orangehrmlive.com/'
    def __init__(self, driver= None, browser='chorme'):
        super().__init__(driver, browser=browser)
        self.open_Index()

    def open_Index(self):
        self.driver.get(self.base_url)
    def username(self):
        self.driver.find_element(By.XPATH,LocatorsIndex.input_userName_xpath).send_keys('Admin')

    def password(self):
        self.driver.find_element(By.XPATH,LocatorsIndex.input_password_xpath).send_keys('admin123')

    def Click_login(self):
        self.driver.find_element(By.XPATH, LocatorsIndex.click_button_Login).click()