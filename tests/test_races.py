def test_list_races(client):
    response = client.get("/races/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["name"] == "Tour de France"


def test_get_race(client):
    response = client.get("/races/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Tour de France"
    assert data["year"] == 2024
    assert len(data["stages"]) == 4


def test_get_race_not_found(client):
    response = client.get("/races/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Race 999 not found"


def test_get_race_stages(client):
    response = client.get("/races/1/stages")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 4
    assert data[0]["number"] == 1
    assert data[0]["stage_type"] == "flat"


def test_get_race_stages_not_found(client):
    response = client.get("/races/999/stages")
    assert response.status_code == 404
