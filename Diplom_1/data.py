from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class BunData:
    NAME = "black bun"
    PRICE = 100

class IngredientData:
    SAUCE_NAME = "hot sauce"
    SAUCE_PRICE = 100
    
    FILLING_NAME = "cutlet"
    FILLING_PRICE = 200

class ReceiptData:
    EXPECTED_RECEIPT = (
        f"(==== {BunData.NAME} ====)\n"
        f"= {INGREDIENT_TYPE_SAUCE.lower()} {IngredientData.SAUCE_NAME} =\n"
        f"(==== {BunData.NAME} ====)\n"
        f"\n"
        f"Price: 300.0" # 100*2 (булка) + 100 (соус)
    )

class BurgerTestData:
    INGREDIENTS_LIST = [
        (INGREDIENT_TYPE_SAUCE, IngredientData.SAUCE_NAME, IngredientData.SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, IngredientData.FILLING_NAME, IngredientData.FILLING_PRICE)
    ]