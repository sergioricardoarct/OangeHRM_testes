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
    def set_Middle(self,Middle):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.input_middle_nome_xpath).send_keys(Middle)
    def set_Last(self,Last):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.input_last_nome_xpath).send_keys(Last)
    def set_Id(self,Id):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.id_employee_xpath).send_keys(Id)
    def Click_Save(self):
        self.driver.find_element(By.XPATH,LocatorsAddEmployee.button_save_xpath).click()

