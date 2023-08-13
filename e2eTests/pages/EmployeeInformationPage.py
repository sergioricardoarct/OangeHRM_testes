from selenium.webdriver.common.by import By

from e2eTests.locators import LocatorsAddEmployee
from e2eTests.pages.PageObject import PageObject


# INIT
class EmployeeInformationPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)


    # SETs

    def set_nane(self, nome):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.input_first_nome_xpath).send_keys(nome)

    def set_middle(self, Middle):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.input_middle_nome_xpath).send_keys(Middle)

    def set_last(self, last):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.input_last_nome_xpath).send_keys(last)

    def set_id(self, nid):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.id_employee_xpath).send_keys(nid)

    def click_save(self):
        self.driver.find_element(By.XPATH, LocatorsAddEmployee.button_save_xpath).click()


