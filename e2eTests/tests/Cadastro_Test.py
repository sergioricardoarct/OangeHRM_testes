import pytest
from e2eTests.pages.IndexPage import pageIndex
from e2eTests.pages.PageDashboard import PageDashboard
from e2eTests.pages.PageEmployeeInformation import PageEmployee


class Test_Cadastro:

    def test_Cadastrar_Funcionario_valido(self,PageDashboard,PageEmployee):

        PageDashboard.clicPIM()

        None1 ='sergio'
        Meedle = 'Ricardo'
        Last = 'Nascimento'

        pageIndex.open_Index()
        PageEmployee.set_Nane(None1)
        PageEmployee.set_Middle(Meedle)
        PageEmployee.set_Last(Last)
        PageEmployee.set_Id()
        PageEmployee.Click_Save()

        assert PageDashboard.is_employee_displayed(first_name, middle_name, last_name)