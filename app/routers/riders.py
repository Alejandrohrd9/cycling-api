from typing import Optional

from fastapi import APIRouter, HTTPException, Query, status

import app.data.riders as store
from app.schemas.rider import Rider, RiderCreate, RiderUpdate

router = APIRouter(prefix="/riders", tags=["riders"])


@router.get("/", response_model=list[Rider])
def list_riders(
    team_id: Optional[int] = Query(None),
    speciality: Optional[str] = Query(None),
):
    items = store.get_all()
    if team_id is not None:
        items = [r for r in items if r["team_id"] == team_id]
    if speciality is not None:
        items = [r for r in items if r["speciality"] == speciality]
    return items


@router.get("/{id}", response_model=Rider)
def get_rider(id: int):
    rider = store.get_by_id(id)
    if not rider:
        raise HTTPException(status_code=404, detail=f"Rider {id} not found")
    return rider


@router.post("/", response_model=Rider, status_code=status.HTTP_201_CREATED)
def create_rider(body: RiderCreate):
    return store.create(body.model_dump())


@router.put("/{id}", response_model=Rider)
def update_rider(id: int, body: RiderUpdate):
    rider = store.update(id, body.model_dump())
    if not rider:
        raise HTTPException(status_code=404, detail=f"Rider {id} not found")
    return rider


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rider(id: int):
    if not store.delete(id):
        raise HTTPException(status_code=404, detail=f"Rider {id} not found")
