import requests
from enum import Enum

from .models import Fruit


HTTP_TIMEOUT_SECONDS = 10

"https://www.fruityvice.com/api/fruit/carbohydrates?min=0&max=1000"


class NutritionSDK:
    def __init__(self):
        self.api_url = "https://www.fruityvice.com/api/fruit"

    class NutritionType(str, Enum):
        PROTEIN = "protein"
        CARBOHYDRATE = "carbohydrates"

    def get_fruits_information_by_nutrition(
        self, nutrition: NutritionType, max: int = 100, min: int = 0
    ):
        """
        Get Fruits with information by nutrition value.
        """
        try:
            response = requests.get(
                self.api_url + f"/{nutrition.value}?min={min}&max={max}",
                timeout=HTTP_TIMEOUT_SECONDS,
            )

            response.raise_for_status()
        except requests.exceptions.ConnectionError as err:
            raise ValueError(
                "Connection error. Check your network connection", str(err)
            )
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 404:
                print(self.api_url)
                raise ValueError("Resource not found")
            else:
                raise

        return [Fruit(**res) for res in response.json()]
