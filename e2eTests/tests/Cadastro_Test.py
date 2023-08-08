from time import time

from e2eTests.pages.IndexPage import PageIndex
import e2eTests.pages.PageDashboard


class Cadastro_Test:

    def test_abrir_inicial(self, open_index, PageDashboard):
        pageIndex = open_index(driver=open_index.driver)
        pageIndex.username()
        open_index.password()
        open_index.click_login()

        PageDashboard = PageDashboard(driver=PageDashboard.driver)
        time(5)
        PageDashboard.clicPIM()
        assert PageDashboard
