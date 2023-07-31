import pytest
from e2eTests.pages.PageDashboard import PageDashboard

@pytest.fixture():
    def Admin_Open():
        print('Acessando pagina de Administrador!')
        open_admin =PageDashboard(browser='Chrome')
        yield open_admin
        print('Saindo do navegador!')
        open_admin.close()

