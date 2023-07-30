from e2eTests.pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from e2eTests.locators import LocatorsEmployee
from selenium.webdriver.common.by import By

from e2eTests.locators import LocatorsDashboard
from e2eTests.pages.PageObject import PageObject


class PageEmployee(PageObject):
    def __init__(self,driver):
        super().__init__(driver)

    def z