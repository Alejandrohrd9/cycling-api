_RACES: list[dict] = [
    {
        "id": 1,
        "name": "Tour de France",
        "country": "France",
        "year": 2024,
        "total_stages": 21,
        "stages": [
            {"number": 1, "name": "Florence - Rimini", "distance_km": 206.0, "stage_type": "flat"},
            {"number": 9, "name": "Trévoux - Villeneuve-sur-Lot", "distance_km": 199.0, "stage_type": "flat"},
            {"number": 14, "name": "Pau - Saint-Lary-Soulan", "distance_km": 151.9, "stage_type": "mountain"},
            {"number": 21, "name": "Monaco - Nice", "distance_km": 33.7, "stage_type": "tt"},
        ],
    },
    {
        "id": 2,
        "name": "Vuelta a España",
        "country": "Spain",
        "year": 2024,
        "total_stages": 21,
        "stages": [
            {"number": 1, "name": "Lisbon - Lisboa", "distance_km": 12.3, "stage_type": "tt"},
            {"number": 8, "name": "Úbeda - Córdoba", "distance_km": 186.0, "stage_type": "flat"},
            {"number": 20, "name": "Villanueva de la Serena - Badajoz", "distance_km": 178.0, "stage_type": "flat"},
        ],
    },
    {
        "id": 3,
        "name": "Giro d'Italia",
        "country": "Italy",
        "year": 2024,
        "total_stages": 21,
        "stages": [
            {"number": 1, "name": "Venaria Reale - Torino", "distance_km": 140.0, "stage_type": "flat"},
            {"number": 6, "name": "Torre del Lago - Rapolano Terme", "distance_km": 180.0, "stage_type": "hilltop"},
            {"number": 15, "name": "Manerba del Garda - Mossano", "distance_km": 222.0, "stage_type": "mountain"},
            {"number": 21, "name": "Roma - Roma", "distance_km": 125.0, "stage_type": "flat"},
        ],
    },
]


def get_all() -> list[dict]:
    return _RACES


def get_by_id(id: int) -> dict | None:
    return next((r for r in _RACES if r["id"] == id), None)
