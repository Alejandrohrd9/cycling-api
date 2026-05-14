from fastapi import FastAPI

from app.routers import teams

app = FastAPI(title="Cycling API", version="1.0.0")

app.include_router(teams.router)


@app.get("/")
def health_check():
    return {"status": "ok", "version": "1.0.0"}
