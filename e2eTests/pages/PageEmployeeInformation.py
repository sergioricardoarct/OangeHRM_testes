from selenium.webdriver.common.by import By

from e2eTests.locators import LocatorsAddEmployee
from e2eTests.pages.PageObject import PageObject


# INIT
class PageEmployee(PageObject):
    def __init__(self, driver):
        super().__init__(driver)

    # SETs
    def set_Nane(self):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.input_first_nome_xpath).send_keys()

    def set_Middle(self):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.input_middle_nome_xpath).send_keys()

    def set_Last(self):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.input_last_nome_xpath).send_keys()

    def set_Id(self):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.id_employee_xpath).send_keys()

    def click_Save(self):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.button_save_xpath).click()
