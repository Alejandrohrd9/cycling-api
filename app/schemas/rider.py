from typing import Literal

from pydantic import BaseModel

Speciality = Literal["climber", "sprinter", "all-rounder", "tt-specialist"]


class RiderBase(BaseModel):
    name: str
    nationality: str
    age: int
    team_id: int
    speciality: Speciality


class RiderCreate(RiderBase):
    pass


class RiderUpdate(RiderBase):
    pass


class Rider(RiderBase):
    id: int

    model_config = {"from_attributes": True}
