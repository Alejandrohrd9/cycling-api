from typing import Literal

from pydantic import BaseModel

ClassificationType = Literal["general", "points", "mountain", "youth"]


class Standing(BaseModel):
    position: int
    rider_id: int
    rider_name: str
    team_name: str
    time_or_points: str


class Classification(BaseModel):
    race_id: int
    type: ClassificationType
    standings: list[Standing]
