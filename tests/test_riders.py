def test_list_riders(client):
    response = client.get("/riders/")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_list_riders_filter_by_team(client):
    response = client.get("/riders/?team_id=1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Tadej Pogačar"


def test_list_riders_filter_by_speciality(client):
    response = client.get("/riders/?speciality=climber")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5
    assert all(r["speciality"] == "climber" for r in data)


def test_get_rider(client):
    response = client.get("/riders/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Tadej Pogačar"


def test_get_rider_not_found(client):
    response = client.get("/riders/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Rider 999 not found"


def test_create_rider(client):
    payload = {
        "name": "Primož Roglič",
        "nationality": "Slovenian",
        "age": 34,
        "team_id": 4,
        "speciality": "all-rounder",
    }
    response = client.post("/riders/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 11
    assert data["name"] == "Primož Roglič"


def test_update_rider(client):
    payload = {
        "name": "Tadej Pogačar",
        "nationality": "Slovenian",
        "age": 26,
        "team_id": 1,
        "speciality": "climber",
    }
    response = client.put("/riders/1", json=payload)
    assert response.status_code == 200
    assert response.json()["age"] == 26


def test_update_rider_not_found(client):
    payload = {"name": "X", "nationality": "X", "age": 30, "team_id": 1, "speciality": "climber"}
    response = client.put("/riders/999", json=payload)
    assert response.status_code == 404


def test_delete_rider(client):
    response = client.delete("/riders/1")
    assert response.status_code == 204
    assert client.get("/riders/1").status_code == 404


def test_delete_rider_not_found(client):
    response = client.delete("/riders/999")
    assert response.status_code == 404
