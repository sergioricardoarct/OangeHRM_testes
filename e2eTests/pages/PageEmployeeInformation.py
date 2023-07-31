from e2eTests.pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from e2eTests.locators import LocatorsEmployee
from e2eTests.locators import LocatorsAddEmployee
from selenium.webdriver.common.by import By

from e2eTests.locators import LocatorsDashboard
from e2eTests.pages.PageObject import PageObject

# INIT
class PageEmployee(PageObject):
    def __init__(self,driver):
        super().__init__(driver)

#SETs
    def set_Nane(self,Nome):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.input_first_nome_xpath).send_keys(Nome)
