from selenium.webdriver.common.by import By
from e2eTests.locators import LocatorsIndex
from e2eTests.pages.PageObject import PageObject


class PageIndex(PageObject):
    base_url = 'https://opensource-demo.orangehrmlive.com/'

    def __init__(self, driver):
        super().__init__(driver)


    def open_Index(self):
        self.driver.get(self.base_url)

    def username(self):
        self.driver.find_element(By.XPATH, LocatorsIndex.input_userName_xpath).send_keys()

    def password(self):
        self.driver.find_element(By.XPATH, LocatorsIndex.input_password_xpath).send_keys()

    def click_login(self):
        self.driver.find_element(By.XPATH, LocatorsIndex.click_button_Login).click()


