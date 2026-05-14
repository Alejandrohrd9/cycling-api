import copy

_SEED: list[dict] = [
    {"id": 1, "name": "Tadej Pogačar", "nationality": "Slovenian", "age": 25, "team_id": 1, "speciality": "climber"},
    {"id": 2, "name": "Jonas Vingegaard", "nationality": "Danish", "age": 27, "team_id": 2, "speciality": "climber"},
    {"id": 3, "name": "Carlos Rodríguez", "nationality": "Spanish", "age": 23, "team_id": 3, "speciality": "climber"},
    {"id": 4, "name": "Geraint Thomas", "nationality": "Welsh", "age": 37, "team_id": 3, "speciality": "all-rounder"},
    {"id": 5, "name": "Enric Mas", "nationality": "Spanish", "age": 29, "team_id": 4, "speciality": "climber"},
    {"id": 6, "name": "Mads Pedersen", "nationality": "Danish", "age": 28, "team_id": 5, "speciality": "sprinter"},
    {"id": 7, "name": "Wout van Aert", "nationality": "Belgian", "age": 29, "team_id": 2, "speciality": "all-rounder"},
    {"id": 8, "name": "Stefan Küng", "nationality": "Swiss", "age": 30, "team_id": 5, "speciality": "tt-specialist"},
    {"id": 9, "name": "Remco Evenepoel", "nationality": "Belgian", "age": 24, "team_id": 3, "speciality": "all-rounder"},
    {"id": 10, "name": "Juan López", "nationality": "Colombian", "age": 26, "team_id": 4, "speciality": "climber"},
]

_store: dict = {"items": [], "next_id": 11}


def _reset() -> None:
    _store["items"] = copy.deepcopy(_SEED)
    _store["next_id"] = 11


_reset()


def get_all() -> list[dict]:
    return _store["items"]


def get_by_id(id: int) -> dict | None:
    return next((r for r in _store["items"] if r["id"] == id), None)


def create(data: dict) -> dict:
    data["id"] = _store["next_id"]
    _store["next_id"] += 1
    _store["items"].append(data)
    return data


def update(id: int, data: dict) -> dict | None:
    for i, r in enumerate(_store["items"]):
        if r["id"] == id:
            data["id"] = id
            _store["items"][i] = data
            return data
    return None


def delete(id: int) -> bool:
    for i, r in enumerate(_store["items"]):
        if r["id"] == id:
            _store["items"].pop(i)
            return True
    return False
