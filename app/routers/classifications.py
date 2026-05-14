from fastapi import APIRouter, HTTPException

import app.data.classifications as store
from app.schemas.classification import Classification

router = APIRouter(prefix="/classifications", tags=["classifications"])


@router.get("/{race_id}", response_model=list[Classification])
def get_by_race(race_id: int):
    result = store.get_by_race(race_id)
    if not result:
        raise HTTPException(status_code=404, detail=f"No classifications found for race {race_id}")
    return result


@router.get("/{race_id}/{classification_type}", response_model=Classification)
def get_by_race_and_type(race_id: int, classification_type: str):
    result = store.get_by_race_and_type(race_id, classification_type)
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"Classification '{classification_type}' not found for race {race_id}",
        )
    return result
