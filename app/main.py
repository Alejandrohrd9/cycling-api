from fastapi import FastAPI

from app.routers import classifications, races, riders, teams

app = FastAPI(title="Cycling API", version="1.0.0")

app.include_router(teams.router)
app.include_router(riders.router)
app.include_router(races.router)
app.include_router(classifications.router)


@app.get("/")
def health_check():
    return {"status": "ok", "version": "1.0.0"}
