import pytest
from e2eTests.pages.IndexPage import PageIndex

@pytest.fixture()
def Index_Open(PageIndex):
    print('Login!')
    open_index = PageIndex.driver(brower='chrome')

    open_index.username('Admin')
    open_index.password('Adm123')
    open_index.click_login()

    yield open_index

