import allure
import pytest
from practicum.database import Database
from practicum.bun import Bun
from practicum.ingredient import Ingredient

class TestDatabase:

    @allure.title('Проверка получения списка доступных булок')
    def test_available_buns_returns_list_of_bun_objects(self):
        database = Database()
        
        with allure.step('Вызвать метод получения булок из базы'):
            buns = database.available_buns()
        
        with allure.step('Проверить, что метод возвращает список'):
            assert isinstance(buns, list), "Метод должен возвращать список"
            
        with allure.step('Проверить, что список не пуст и содержит объекты Bun'):
            assert len(buns) > 0, "Список булок не должен быть пустым"
            assert isinstance(buns[0], Bun), "Элементы списка должны быть экземплярами класса Bun"

    @allure.title('Проверка получения списка доступных ингредиентов')
    def test_available_ingredients_returns_list_of_ingredient_objects(self):
        database = Database()
        
        with allure.step('Вызвать метод получения ингредиентов из базы'):
            ingredients = database.available_ingredients()
            
        with allure.step('Проверить, что метод возвращает список'):
            assert isinstance(ingredients, list), "Метод должен возвращать список"
            
        with allure.step('Проверить, что список не пуст и содержит объекты Ingredient'):
            assert len(ingredients) > 0, "Список ингредиентов не должен быть пустым"
            assert isinstance(ingredients[0], Ingredient), "Элементы списка должны быть экземплярами класса Ingredient"

    @allure.title('Проверка корректности данных булок в базе')
    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_get_specific_bun_data(self, index, expected_name, expected_price):
        database = Database()
        
        with allure.step(f'Получить список булок и выбрать элемент с индексом {index}'):
            buns = database.available_buns()
            bun = buns[index]
            
        with allure.step(f'Проверить, что имя булки — "{expected_name}" и цена — {expected_price}'):
            assert bun.get_name() == expected_name
            assert bun.get_price() == expected_price

    @allure.title('Проверка типов и названий ингредиентов')
    @pytest.mark.parametrize("index, expected_type, expected_name", [
        (0, "SAUCE", "hot sauce"),
        (3, "FILLING", "cutlet")
    ])
    def test_ingredient_data_in_database(self, index, expected_type, expected_name):
        database = Database()
        
        with allure.step(f'Получить список ингредиентов и выбрать элемент с индексом {index}'):
            ingredients = database.available_ingredients()
            ingredient = ingredients[index]
            
        with allure.step(f'Проверить тип "{expected_type}" и название "{expected_name}"'):
            # Здесь мы проверяем работу методов get_type() и get_name() объекта
            assert ingredient.get_type() == expected_type
            assert ingredient.get_name() == expected_name