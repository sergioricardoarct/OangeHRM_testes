from datetime import time

import pytest
from e2eTests.pages.IndexPage import IndexPage
from e2eTests.pages.EmployeeInformationPage import EmployeeInformationPage

@pytest.fixture()
def index_open():
    print("Log in!")
    open_index = IndexPage()

    open_index.username('Admin')
    open_index.password('admin123')
    open_index.click_login()

    yield open_index

@pytest.fixture()
def employee_open():
