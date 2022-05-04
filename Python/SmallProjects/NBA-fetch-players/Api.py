import requests
import json
from types import SimpleNamespace

BASE_URL = "https://data.nba.net/10s/prod/v1"


def convert_json_to_object(text: str) -> object:
    return json.loads(text, object_hook=lambda d: SimpleNamespace(**d))


def get_players(year: int) -> json:
    r = requests.get(f"{BASE_URL}/{year}/players.json")
    return convert_json_to_object(text=r.text)


def write_file(season: int):
    with open(f"./NBA_PLAYERS_{season}.csv", "w+") as file:
        data = get_players(year=season)
        player_ob = data.league.standard
        file.write(
            "Position, First, Last, Height, Active, Jersey, DateOfBirth, Country\n")
        for i in player_ob:
            file.write(f"{i.pos}, {i.firstName}, {i.lastName}, {i.heightMeters}, {i.isActive}, {i.jersey}, {i.dateOfBirthUTC}, {i.country}\n")
