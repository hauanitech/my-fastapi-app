from dataclasses import dataclass
import json
from fastapi import FastAPI, HTTPException

with open("pokemon.json", "r") as file:
    pokemon_data = json.load(file)

list_pokemons = []
for pokemon in pokemon_data:
    list_pokemons.append(pokemon)

@dataclass
class Pokemon():
    id: int
    name: str
    types: list[str]
    total: int
    hp: int
    attack: int
    defense: int
    attack_special: int
    defense_special: int
    speed: int
    evolution_id: int | None = None

app = FastAPI()

@app.get("/total_pokemons")
def get_total_pokemons():
    return f"{len(list_pokemons)} pokemons found"

@app.get("/all_pokemons")
def get_all_pokemons():
    return [Pokemon(**pokemon) for pokemon in list_pokemons]

@app.get("/pokemon/{id}")
def get_pokemon_by_id(id: int):
    for pokemon in list_pokemons:
        if pokemon["id"] == id:
            return Pokemon(**pokemon)
    raise HTTPException(status_code=404, detail="Pokemon not found")