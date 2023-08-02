import pytest
from e2eTests.pages.IndexPage import pageIndex
from e2eTests.pages.PageDashboard import PageDashboard
from e2eTests.pages.PageEmployeeInformation import PageEmployee


class Test_Cadastro:

    def Cadastrar_Funcionario_valido(self,clicPIM,PageEmployee,loginAdmin):
        clicPIM.click()

        nome ='sergio'
        meedle = 'Ricardo'
        last = 'Nascimento'

        PageEmployee.driver(driver = loginAdmin())
        PageEmployee.set_Nane(nome)
        PageEmployee.set_Middle(meedle)
        PageEmployee.set_Last(last)
        PageEmployee.set_Id()
        PageEmployee.Click_Save()

        assert PageEmployee.Click_Save()