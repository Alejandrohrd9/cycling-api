import copy

_SEED: list[dict] = [
    {"id": 1, "name": "UAE Team Emirates", "country": "UAE", "founded_year": 2017, "budget_millions": 45.0},
    {"id": 2, "name": "Jumbo-Visma", "country": "Netherlands", "founded_year": 2016, "budget_millions": 38.5},
    {"id": 3, "name": "Ineos Grenadiers", "country": "United Kingdom", "founded_year": 2010, "budget_millions": 50.0},
    {"id": 4, "name": "Movistar Team", "country": "Spain", "founded_year": 2011, "budget_millions": 32.0},
    {"id": 5, "name": "Lidl-Trek", "country": "United States", "founded_year": 1995, "budget_millions": 28.0},
]

_store: dict = {"items": [], "next_id": 6}


def _reset() -> None:
    _store["items"] = copy.deepcopy(_SEED)
    _store["next_id"] = 6


_reset()


def get_all() -> list[dict]:
    return _store["items"]


def get_by_id(id: int) -> dict | None:
    return next((t for t in _store["items"] if t["id"] == id), None)


def create(data: dict) -> dict:
    data["id"] = _store["next_id"]
    _store["next_id"] += 1
    _store["items"].append(data)
    return data


def update(id: int, data: dict) -> dict | None:
    for i, t in enumerate(_store["items"]):
        if t["id"] == id:
            data["id"] = id
            _store["items"][i] = data
            return data
    return None


def delete(id: int) -> bool:
    for i, t in enumerate(_store["items"]):
        if t["id"] == id:
            _store["items"].pop(i)
            return True
    return False
