import allure
import pytest
from praktikum.ingredient import Ingredient
from data import IngredientData
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @allure.title('Проверка получения названия ингредиента')
    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, IngredientData.SAUCE_NAME, IngredientData.SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, IngredientData.FILLING_NAME, IngredientData.FILLING_PRICE)
    ])
    def test_get_name_ingredient_success(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_name() == name

    @allure.title('Проверка получения стоимости ингредиента')
    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, IngredientData.SAUCE_NAME, IngredientData.SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, IngredientData.FILLING_NAME, IngredientData.FILLING_PRICE)
    ])
    def test_get_price_ingredient_success(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_price() == price

    @allure.title('Проверка получения типа ингредиента')
    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, IngredientData.SAUCE_NAME, IngredientData.SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, IngredientData.FILLING_NAME, IngredientData.FILLING_PRICE)
    ])
    def test_get_type_ingredient_success(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_type() == ing_type