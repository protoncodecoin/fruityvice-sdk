from pydantic import BaseModel


class NutritionsDetail(BaseModel):
    calories: int
    fat: float
    sugar: float
    carbohydrates: float
    protein: float


class Fruit(BaseModel):
    name: str
    id: int
    family: str
    order: str
    genus: str
    nutritions: NutritionsDetail
