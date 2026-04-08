import allure
import pytest

class TestDatabase:

    @allure.title('Проверка количества доступных булок в базе')
    def test_available_buns_count(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    @allure.title('Проверка количества доступных ингредиентов в базе')
    def test_available_ingredients_count(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    @allure.title('Проверка названий и цен булок в базе')
    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_get_specific_bun_data(self, database, index, expected_name, expected_price):
        buns = database.available_buns()
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    @allure.title('Проверка типов и названий ингредиентов')
    @pytest.mark.parametrize("index, expected_type, expected_name", [
        (0, "SAUCE", "hot sauce"),
        (3, "FILLING", "cutlet")
    ])
    def test_ingredient_data_in_database(self, database, index, expected_type, expected_name):
        ingredients = database.available_ingredients()
        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name