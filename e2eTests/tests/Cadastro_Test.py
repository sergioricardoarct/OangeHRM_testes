from time import time

from e2eTests.pages.IndexPage import PageIndex


class Test_Cadastro:

    def test_abrir_inicial(self, open_index):
        pageIndex = PageIndex(driver=open_index)
        pageIndex.open_Index()
        time(10)
