from datetime import time

import pytest
from e2eTests.pages.IndexPage import IndexPage
from e2eTests.pages.EmployeeInformationPage import EmployeeInformationPage
from e2eTests.pages.PIMPage import PimPage

@pytest.fixture()
def index_open():
    print("Log in!")
    open_index = IndexPage()

    open_index.username('Admin')
    open_index.password('admin123')
    open_index.click_login()

    yield open_index

@pytest.fixture()
def open_pim():
    open_PIM = PimPage(browser='chrome')
    open_PIM.click_add()
    yield open_pim