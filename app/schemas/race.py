from typing import Literal

from pydantic import BaseModel

StageType = Literal["flat", "mountain", "tt", "hilltop"]


class Stage(BaseModel):
    number: int
    name: str
    distance_km: float
    stage_type: StageType


class Race(BaseModel):
    id: int
    name: str
    country: str
    year: int
    total_stages: int
    stages: list[Stage]
