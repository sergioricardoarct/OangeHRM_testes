import pytest
from e2eTests.pages.IndexPage import pageIndex

@pytest.fixture()
def Index_Open():
    print('Login!')
    open_index = pageIndex(browser='Chrome')
    yield open_index

@pytest.fixture
def loginAdmin(Index_Open):
    print('Logando!')
    pageIndex.username()
    pageIndex.password()
    pageIndex.Click_login()
    yield loginAdmin