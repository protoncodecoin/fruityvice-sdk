from pydantic import BaseModel


class NutritionsDetail(BaseModel):
    calories: int
    fat: float
    sugar: float
    carbohydates: float
    protein: float


class Nutrition(BaseModel):
    name: str
    id: int
    family: str
    order: str
    genus: str
    nutritions: NutritionsDetail
