from e2eTests.pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from e2eTests.locators import LocatorsAdmin
from selenium.webdriver.common.by import By

from e2eTests.locators import LocatorsAdmin
from e2eTests.pages.PageObject import PageObject


class PageAdmin(PageObject):
    # SETUP
    base_url = 'https://opensource-demo.orangehrmlive.com/'

    def __init__(self, driver=None, browser='chorme'):
        super().__init__(driver, browser=browser)
        self.opemAdmin()

    def opemAdmin(self):
        self.driver.get(self.base_url)

    # SET

    def clicPIM(self):
        self.driver.find_element(By.XPATH, LocatorsAdmin.botao_pim_xpath).click()
