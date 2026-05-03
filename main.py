from fastapi import FastAPI, HTTPException

from models import CharacterUpdate, WeaponBase

app = FastAPI(
    title="Elden Ring  API",
    description="Elden Ring build manager API",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {"message": "Elden Ring Build API"}



# ── CHARACTER ─────────────────────────────────────────────────────────────────
@app.post("/character", response_model=list[CharacterID], tags=["Character"])
async def create_character(character: CharacterBase):
    return createCharacter(character)

@app.get("/character", response_model=list[CharacterID], tags=["Character"])
async def show_characters():
    return showCharacters()

@app.get("/character/filter/class", response_model=list[CharacterID], tags=["Character"])
async def filter_characters(characters_class: str):
    return filterCharacters(characters_class)

@app.get("/character/search/name", response_model=CharacterID, tags=["Character"])
async def search_character(name: str):
    character= searchCharacterByName(name)
    if not character:
        raise HTTPException(status_code=404, detail=f"Character '{name}' not found")
    return character

@app.get("/character/{id}", response_model=CharacterID, tags=["Character"])
async def show_character(id: str):
    character= findCharacter(id)
    if not character:
        raise HTTPException(status_code=404, detail=f"Character '{id}' Character not found")
    return character

@app.patch("/character/{id}", response_model=CharacterID, tags=["Character"])
async def update_character(id: int , character: CharacterUpdate):
    updated = updateCharacter(id, character)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Character '{id}' Character not found")
    return updated

@app.delete("/character/{id}", response_model=CharacterID, tags=["Characters"])
async def delete_character(id: int):
    deleted = deleteCharacter(id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"{id} Character not found")
    return deleted

# ── WEAPON────────────────────────────────────────────────────────
@app.post("/weapon", response_model=WeaponID, tags=["Weapons"])
async def create_weapon(weapon: WeaponBase):
    return createWeapon(weapon)

@app.get("/weapon", response_model=list[WeaponID], tags=["Weapons"])
async def show_weapons():
    return showWeapons()

@app.get("/weapon/filter/Type", response_model=list[WeaponID], tags=["Weapons"])
async def filter_weapons(weapon_type: str):
    return filterWeaponsByType(weapon_type)

@app.get("/weapon/search/name", response_model=WeaponID, tags=["Weapons"])
async def search_weapon(name: str):
    weapon= searchWeaponByName(name)
    if not weapon:
        raise HTTPException(status_code=404, detail=f"Weapon '{name}' not found")
    return weapon

@app.get("/weapon/{id}", response_model=WeaponID, tags=["Weapons"])
async def show_weapon(id: int):
    weapon= findWeapon(id)
    if not weapon:
        raise HTTPException(status_code=404, detail=f"'{id}' Weapon not found")
    return weapon

@app.patch("/weapon/{id}", response_model=WeaponID, tags=["Weapons"])
async def update_weapon(id: int , weapon: WeaponUpdate):
    updated = updateWeapon(id, weapon)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Character '{id}' Character not found")
    return updated

@app.delete("/weapon/{id}", response_model=WeaponID, tags=["Weapons"])
async def delete_weapon(id: int):
    deleted = deleteWeapon(id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"{id} Weapon not found")
    return deleted


# ── BUILD ─────────────────────────────────────────────────────────────────────