import pytest
from e2eTests.pages.IndexPage import pageIndex

@pytest.fixture()
def Index_Open():
    print('Login!')
    open_index = pageIndex(browser='Chrome')
    yield open_index
