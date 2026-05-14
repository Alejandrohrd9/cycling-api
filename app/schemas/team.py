from pydantic import BaseModel


class TeamBase(BaseModel):
    name: str
    country: str
    founded_year: int
    budget_millions: float


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    pass


class Team(TeamBase):
    id: int

    model_config = {"from_attributes": True}
