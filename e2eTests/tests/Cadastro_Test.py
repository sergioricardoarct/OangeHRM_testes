from e2eTests.pages.DashboardPage import DashboardPage
from e2eTests.pages.EmployeeInformationPage import EmployeeInformationPage


class Cadastro_Test:

    def test_abrir_inicial(self, index_open):
        PageDashboard = DashboardPage(driver=index_open.driver)
        PageDashboard.clickPIM()
        assert PageDashboard

    def test_cadastrar_funcionario_valido(self, employee_open):
