from selenium.webdriver.common.by import By
from e2eTests.locators import LocatorsIndex
from e2eTests.pages.PageObject import PageObject


class IndexPage(PageObject):
    base_url = 'https://opensource-demo.orangehrmlive.com/'

    def __init__(self, driver= None, browser='chrome'):
        super().__init__(driver, browser=browser)
        self.open_index()
    def open_index(self):
        self.driver.get(self.base_url)

    def username(self, user):
        self.driver.find_element(By.XPATH, LocatorsIndex.input_userName_xpath).send_keys(user)

    def password(self, word):
        self.driver.find_element(By.XPATH, LocatorsIndex.input_password_xpath).send_keys(word)

    def click_login(self):
        self.driver.find_element(By.XPATH, LocatorsIndex.click_button_Login).click()
