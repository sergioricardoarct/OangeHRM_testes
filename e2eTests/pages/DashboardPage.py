from selenium.webdriver.common.by import By

from e2eTests.locators import LocatorsDashboard
from e2eTests.pages.PageObject import PageObject


class DashboardPage(PageObject):

    def __init__(self, driver):
        super().__init__(driver)

    # SET

    def clickPIM(self):
        print('Click in PIM')
        self.driver.find_element(By.XPATH, LocatorsDashboard.botao_pim_xpath).click()
