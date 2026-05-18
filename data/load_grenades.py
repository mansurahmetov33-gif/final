import json
from models.grenade import Grenade


with open("data/grenades.json", "r", encoding="utf-8") as file:
    data = json.load(file)


grenades = {}


for key, grenade_data in data.items():

    grenades[key] = Grenade(
        path=grenade_data["path"],
        title=grenade_data["title"],
        lineup=grenade_data.get("lineup"),
        description=grenade_data.get("description")
    )