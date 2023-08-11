from e2eTests.pages.DashboardPage import DashboardPage


class Cadastro_Test:

    def test_abrir_inicial(self, index_open):
        PageDashboard = DashboardPage(driver=index_open.driver)
        PageDashboard.clickPIM()
        assert PageDashboard
