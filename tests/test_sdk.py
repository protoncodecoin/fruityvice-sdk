from src.nutrition_sdk.sdk import NutritionSDK
import responses
from responses import matchers
import requests

api_url = "https://example.com"


def test_sdk():
    sdk = NutritionSDK()
    assert sdk.api_url == "https://www.fruityvice.com/api/fruit"


@responses.activate
def test_sdk_get_fruits_information_by_nutriiton():
    responses.add(
        responses.GET,
        api_url + "/carbohydrates?min=0&max=100",
        json=[
            {
                "name": "Persimmon",
                "id": 52,
                "family": "Ebenaceae",
                "order": "Rosales",
                "genus": "Diospyros",
                "nutritions": {
                    "calories": 81,
                    "fat": 0,
                    "sugar": 18,
                    "carbohydrates": 18,
                    "protein": 0,
                },
            },
            {
                "name": "Strawberry",
                "id": 3,
                "family": "Rosaceae",
                "order": "Rosales",
                "genus": "Fragaria",
                "nutritions": {
                    "calories": 29,
                    "fat": 0.4,
                    "sugar": 5.4,
                    "carbohydrates": 5.5,
                    "protein": 0.8,
                },
            },
        ],
        status=200,
    )

    sdk = NutritionSDK()
    fruits_info = sdk.get_fruits_information_by_nutrition(
        nutrition=sdk.NutritionType.CARBOHYDRATE
    )

    assert len(fruits_info) == 2


@responses.activate
def test_sdk_get_fruits_information_by_nutrition_error():
    responses.add(
        responses.GET,
        api_url + "/carbohydrates?min=0&max=100",
        body=requests.exceptions.ConnectionError(),
    )

    sdk = NutritionSDK()

    try:
        sdk.get_fruits_information_by_nutrition(
            nutrition=sdk.NutritionType.CARBOHYDRATE
        )
    except ValueError as err:
        assert "Connection error" in str(err)
    else:
        assert False, "Expected ValueError"


@responses.activate
def test_sdk_get_fruits_information_by_nutrition_with_protein():
    responses.add(
        responses.GET,
        api_url + f"/protein?min=0&max=100",
        json=[
            {
                "name": "Persimmon",
                "id": 52,
                "family": "Ebenaceae",
                "order": "Rosales",
                "genus": "Diospyros",
                "nutritions": {
                    "calories": 81,
                    "fat": 0,
                    "sugar": 18,
                    "carbohydrates": 18,
                    "protein": 0,
                },
            },
            {
                "name": "Strawberry",
                "id": 3,
                "family": "Rosaceae",
                "order": "Rosales",
                "genus": "Fragaria",
                "nutritions": {
                    "calories": 29,
                    "fat": 0.4,
                    "sugar": 5.4,
                    "carbohydrates": 5.5,
                    "protein": 0.8,
                },
            },
        ],
    )

    sdk = NutritionSDK()
    result = sdk.get_fruits_information_by_nutrition(
        nutrition=sdk.NutritionType.PROTEIN
    )

    assert len(result) == 2
    assert result[0]["name"] == "Persimmon"
    assert result[0]["id"] == 52
