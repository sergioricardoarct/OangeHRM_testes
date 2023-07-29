from selenium import webdriver
from e2eTests.pages.PageObject import PageObject
from e2eTests.locators.LocatorsAdmin

class PageAdmin(PageObject):
    def __init__(self,driver):
        super().__init__(driver)


