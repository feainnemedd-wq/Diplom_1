import allure
import pytest
from praktikum.bun import Bun
from data import BunData

class TestBun:

    @allure.title('Проверка получения названия булки')
    @pytest.mark.parametrize("name, price", [
        (BunData.NAME, BunData.PRICE),
        ("special bun", 500.5)
    ])
    def test_get_name_bun_success(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @allure.title('Проверка получения стоимости булки')
    @pytest.mark.parametrize("name, price", [
        (BunData.NAME, BunData.PRICE),
        ("cheap bun", 0.0)
    ])
    def test_get_price_bun_success(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price