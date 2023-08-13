from time import time

from e2eTests.pages.DashboardPage import DashboardPage
from e2eTests.pages.EmployeeInformationPage import EmployeeInformationPage
from e2eTests.pages.PIMPage import PimPage


class Cadastro_Test:

    def test_abrir_inicial(self, index_open):
        PageDashboard = DashboardPage(driver=index_open.driver)
        PageDashboard.clickPIM()
        assert PageDashboard

    def test_cadastrar_funcionario_valido(self, index_open, open_pim):
        PageDashboard = DashboardPage(driver=index_open.driver)
        PageDashboard.clickPIM()
        PIMPage = PimPage(driver=open_pim.driver)
        PIMPage.click_add()

