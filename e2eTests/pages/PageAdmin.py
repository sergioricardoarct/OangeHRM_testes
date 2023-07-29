from selenium import webdriver
from e2eTests.pages.PageObject import PageObject

class PageAdmin(PageObject):

# SETUP
    base_url = 'https://opensource-demo.orangehrmlive.com/'

    def __init__(self,driver=None, browser='chome'):
        super().__init__(driver, browser=browser)
        self.opemAdmin()

    def opemAdmin(self):
        self.driver.get(self.base_url)

#SET

