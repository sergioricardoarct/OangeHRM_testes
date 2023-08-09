from time import time

from e2eTests.pages.IndexPage import PageIndex
import e2eTests.pages.PageDashboard


class Cadastro_Test:

    def test_abrir_inicial(self,Index_Open, PageDashboard):
        pageIndex = Index_Open(driver=Index_Open.driver)
        pageIndex.open_Index()

        PageDashboard = PageDashboard(driver=PageDashboard.driver)
        time(5)
        PageDashboard.clicPIM()
        assert PageDashboard
