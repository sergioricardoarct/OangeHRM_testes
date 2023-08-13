from selenium.webdriver.common.by import By
from e2eTests.pages.PageObject import PageObject
from e2eTests.locators import LocatorsPIM

class PimPage(PageObject):
    def __init__(self, driver= None, browser='chrome'):
        super().__init__(driver,browser=browser)


    def click_add(self):
        self.driver.find_element(By.XPATH, LocatorsPIM.PIM_ButtonAdd_Xpath).click()
