import pytest
from e2eTests.pages.IndexPage import pageIndex

@pytest.fixture()
def  :
    print('Login!')
    open_index = pageIndex(browser='Chrome')
    yield open_index

@pytest.fixture()
def open