def test_list_teams(client):
    response = client.get("/teams/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5
    assert data[0]["name"] == "UAE Team Emirates"


def test_get_team(client):
    response = client.get("/teams/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "UAE Team Emirates"
    assert data["country"] == "UAE"


def test_get_team_not_found(client):
    response = client.get("/teams/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Team 999 not found"


def test_create_team(client):
    payload = {
        "name": "Alpecin-Deceuninck",
        "country": "Belgium",
        "founded_year": 2013,
        "budget_millions": 22.5,
    }
    response = client.post("/teams/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 6
    assert data["name"] == "Alpecin-Deceuninck"


def test_update_team(client):
    payload = {
        "name": "UAE Team Emirates",
        "country": "UAE",
        "founded_year": 2017,
        "budget_millions": 50.0,
    }
    response = client.put("/teams/1", json=payload)
    assert response.status_code == 200
    assert response.json()["budget_millions"] == 50.0


def test_update_team_not_found(client):
    payload = {"name": "Ghost", "country": "X", "founded_year": 2000, "budget_millions": 1.0}
    response = client.put("/teams/999", json=payload)
    assert response.status_code == 404


def test_delete_team(client):
    response = client.delete("/teams/1")
    assert response.status_code == 204
    assert client.get("/teams/1").status_code == 404


def test_delete_team_not_found(client):
    response = client.delete("/teams/999")
    assert response.status_code == 404
