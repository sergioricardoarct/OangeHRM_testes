from e2eTests.pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from e2eTests.locators import LocatorsDashboard
from selenium.webdriver.common.by import By

from e2eTests.locators import LocatorsDashboard
from e2eTests.pages.PageObject import PageObject


class PageDashboard(PageObject):
    # SETUP
    base_url = 'https://opensource-demo.orangehrmlive.com/'

    def __init__(self, driver=None, browser='chorme'):
        super().__init__(driver, browser=browser)
        self.openDashboard()

    def openDashboard(self):
        self.driver.get(self.base_url)

    # SET

    def clicPIM(self):
        print('Click in PIM')
        self.driver.find_element(By.XPATH, LocatorsDashboard.botao_pim_xpath).click()
