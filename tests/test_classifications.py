def test_get_classifications_for_race(client):
    response = client.get("/classifications/1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    types = {c["type"] for c in data}
    assert types == {"general", "points"}


def test_get_classifications_race_not_found(client):
    response = client.get("/classifications/999")
    assert response.status_code == 404


def test_get_general_classification(client):
    response = client.get("/classifications/1/general")
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "general"
    assert data["race_id"] == 1
    assert data["standings"][0]["position"] == 1
    assert data["standings"][0]["rider_name"] == "Tadej Pogačar"


def test_get_points_classification(client):
    response = client.get("/classifications/2/points")
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "points"
    assert data["standings"][0]["rider_name"] == "Mads Pedersen"


def test_get_classification_type_not_found(client):
    response = client.get("/classifications/1/youth")
    assert response.status_code == 404
    assert "youth" in response.json()["detail"]
