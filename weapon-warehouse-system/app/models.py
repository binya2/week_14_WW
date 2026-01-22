from typing import Optional, Literal

from pydantic import BaseModel, Field


class Weapons(BaseModel):
    weapon_id: str = Field(..., min_length=5, max_length=20)
    weapon_name: str
    weapon_type: str
    range_km: int
    weight_kg: float
    manufacturer: Optional[str] = None
    origin_country: str
    storage_location: str
    year_estimated: int

class WeaponsDB(Weapons):
    risk_level:str = Literal["low", "medium", "high","extreme"]

class Response(BaseModel):
    status: str
    inserted_records: int

