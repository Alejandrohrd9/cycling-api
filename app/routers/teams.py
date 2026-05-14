from fastapi import APIRouter, HTTPException, status

import app.data.teams as store
from app.schemas.team import Team, TeamCreate, TeamUpdate

router = APIRouter(prefix="/teams", tags=["teams"])


@router.get("/", response_model=list[Team])
def list_teams():
    return store.get_all()


@router.get("/{id}", response_model=Team)
def get_team(id: int):
    team = store.get_by_id(id)
    if not team:
        raise HTTPException(status_code=404, detail=f"Team {id} not found")
    return team


@router.post("/", response_model=Team, status_code=status.HTTP_201_CREATED)
def create_team(body: TeamCreate):
    return store.create(body.model_dump())


@router.put("/{id}", response_model=Team)
def update_team(id: int, body: TeamUpdate):
    team = store.update(id, body.model_dump())
    if not team:
        raise HTTPException(status_code=404, detail=f"Team {id} not found")
    return team


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_team(id: int):
    if not store.delete(id):
        raise HTTPException(status_code=404, detail=f"Team {id} not found")
