import pytest
from unittest.mock import Mock
from data import BunData, IngredientData
from praktikum.database import Database

@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = BunData.NAME
    mock.get_price.return_value = BunData.PRICE
    return mock

@pytest.fixture
def mock_sauce():
    mock = Mock()
    mock.get_name.return_value = IngredientData.SAUCE_NAME
    mock.get_price.return_value = IngredientData.SAUCE_PRICE
    mock.get_type.return_value = "SAUCE"
    return mock

@pytest.fixture
def mock_filling():
    mock = Mock()
    mock.get_name.return_value = IngredientData.FILLING_NAME
    mock.get_price.return_value = IngredientData.FILLING_PRICE
    mock.get_type.return_value = "FILLING"
    return mock

@pytest.fixture
def database():
    return Database()