import pytest
from e2eTests.pages.IndexPage import IndexPage


@pytest.fixture()
def index_open():
    open_index = IndexPage()

    open_index.username('Admin')
    open_index.password('admin123')
    open_index.click_login()

    yield open_index

