_CLASSIFICATIONS: list[dict] = [
    {
        "race_id": 1,
        "type": "general",
        "standings": [
            {"position": 1, "rider_id": 1, "rider_name": "Tadej Pogačar", "team_name": "UAE Team Emirates", "time_or_points": "87:23:14"},
            {"position": 2, "rider_id": 2, "rider_name": "Jonas Vingegaard", "team_name": "Jumbo-Visma", "time_or_points": "+6:17"},
            {"position": 3, "rider_id": 3, "rider_name": "Carlos Rodríguez", "team_name": "Ineos Grenadiers", "time_or_points": "+10:54"},
        ],
    },
    {
        "race_id": 1,
        "type": "points",
        "standings": [
            {"position": 1, "rider_id": 1, "rider_name": "Tadej Pogačar", "team_name": "UAE Team Emirates", "time_or_points": "452 pts"},
            {"position": 2, "rider_id": 6, "rider_name": "Mads Pedersen", "team_name": "Lidl-Trek", "time_or_points": "288 pts"},
            {"position": 3, "rider_id": 7, "rider_name": "Wout van Aert", "team_name": "Jumbo-Visma", "time_or_points": "241 pts"},
        ],
    },
    {
        "race_id": 2,
        "type": "general",
        "standings": [
            {"position": 1, "rider_id": 9, "rider_name": "Remco Evenepoel", "team_name": "Ineos Grenadiers", "time_or_points": "82:51:06"},
            {"position": 2, "rider_id": 5, "rider_name": "Enric Mas", "team_name": "Movistar Team", "time_or_points": "+2:36"},
            {"position": 3, "rider_id": 10, "rider_name": "Juan López", "team_name": "Movistar Team", "time_or_points": "+4:10"},
        ],
    },
    {
        "race_id": 2,
        "type": "points",
        "standings": [
            {"position": 1, "rider_id": 6, "rider_name": "Mads Pedersen", "team_name": "Lidl-Trek", "time_or_points": "198 pts"},
            {"position": 2, "rider_id": 9, "rider_name": "Remco Evenepoel", "team_name": "Ineos Grenadiers", "time_or_points": "175 pts"},
            {"position": 3, "rider_id": 7, "rider_name": "Wout van Aert", "team_name": "Jumbo-Visma", "time_or_points": "156 pts"},
        ],
    },
    {
        "race_id": 3,
        "type": "general",
        "standings": [
            {"position": 1, "rider_id": 1, "rider_name": "Tadej Pogačar", "team_name": "UAE Team Emirates", "time_or_points": "88:12:54"},
            {"position": 2, "rider_id": 3, "rider_name": "Carlos Rodríguez", "team_name": "Ineos Grenadiers", "time_or_points": "+9:56"},
            {"position": 3, "rider_id": 4, "rider_name": "Geraint Thomas", "team_name": "Ineos Grenadiers", "time_or_points": "+14:23"},
        ],
    },
    {
        "race_id": 3,
        "type": "points",
        "standings": [
            {"position": 1, "rider_id": 1, "rider_name": "Tadej Pogačar", "team_name": "UAE Team Emirates", "time_or_points": "367 pts"},
            {"position": 2, "rider_id": 6, "rider_name": "Mads Pedersen", "team_name": "Lidl-Trek", "time_or_points": "214 pts"},
            {"position": 3, "rider_id": 7, "rider_name": "Wout van Aert", "team_name": "Jumbo-Visma", "time_or_points": "189 pts"},
        ],
    },
]


def get_by_race(race_id: int) -> list[dict]:
    return [c for c in _CLASSIFICATIONS if c["race_id"] == race_id]


def get_by_race_and_type(race_id: int, classification_type: str) -> dict | None:
    return next(
        (c for c in _CLASSIFICATIONS if c["race_id"] == race_id and c["type"] == classification_type),
        None,
    )
