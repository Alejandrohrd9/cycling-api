import pytest
from fastapi.testclient import TestClient

import app.data.teams as teams_store
import app.data.riders as riders_store
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_data():
    teams_store._reset()
    riders_store._reset()
