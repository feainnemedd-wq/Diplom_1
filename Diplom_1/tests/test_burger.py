import allure
import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import ReceiptData, BurgerTestData

class TestBurger:

    @allure.title('Установка булок в бургер')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Добавление ингредиента в бургер')
    @pytest.mark.parametrize("type, name, price", BurgerTestData.INGREDIENTS_LIST)
    def test_add_ingredient(self, type, name, price):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    @allure.title('Удаление ингредиента из бургера')
    def test_remove_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert mock_sauce not in burger.ingredients
        assert len(burger.ingredients) == 0

    @allure.title('Перемещение ингредиента в списке')
    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)  # index 0
        burger.add_ingredient(mock_filling) # index 1
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_sauce
        assert burger.ingredients[0] == mock_filling

    @allure.title('Расчет итоговой стоимости бургера')
    def test_get_price(self, mock_bun, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun) # 100 * 2
        burger.add_ingredient(mock_sauce) # + 100
        # Ожидаем 300.0 (float)
        assert burger.get_price() == 300.0

    @allure.title('Проверка формирования чека')
    def test_get_receipt(self, mock_bun, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        
        receipt = burger.get_receipt()
        
        assert f"(==== {mock_bun.get_name()} ====)" in receipt
        assert f"= {mock_sauce.get_type().lower()} {mock_sauce.get_name()} =" in receipt
        assert "Price: 300" in receipt