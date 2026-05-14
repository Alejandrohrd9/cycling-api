from fastapi import APIRouter, HTTPException

import app.data.races as store
from app.schemas.race import Race, Stage

router = APIRouter(prefix="/races", tags=["races"])


@router.get("/", response_model=list[Race])
def list_races():
    return store.get_all()


@router.get("/{id}", response_model=Race)
def get_race(id: int):
    race = store.get_by_id(id)
    if not race:
        raise HTTPException(status_code=404, detail=f"Race {id} not found")
    return race


@router.get("/{id}/stages", response_model=list[Stage])
def get_race_stages(id: int):
    race = store.get_by_id(id)
    if not race:
        raise HTTPException(status_code=404, detail=f"Race {id} not found")
    return race["stages"]
