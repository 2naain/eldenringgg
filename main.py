from fastapi import FastAPI, HTTPException

from models.character import CharacterBase, CharacterID, CharacterUpdate
from models.weapon import WeaponBase, WeaponID, WeaponUpdate
from models.build import BuildBase, BuildID, BuildUpdate, BuildDetail


from operations.operations_character import (
    createCharacter, showCharacters, findCharacter,
    updateCharacter, deleteCharacter,
    filterCharactersByClass, searchCharacterByName
)
from operations.operations_weapon import (
    createWeapon, showWeapons, findWeapon,
    updateWeapon, deleteWeapon,
    filterWeaponsByType, searchWeaponByName
)
from operations.operations_build import (
    createBuild, showBuilds, findBuild,
    updateBuild, deleteBuild,
    filterBuildsByFocus,
    showBuildsDetail, findBuildDetail
)


app = FastAPI(
    title="Elden Ring Build API",
    description="API to manage characters, weapons and builds from Elden Ring.",
    version="1.0.0",
)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Elden Ring Build API"}


# ── CHARACTER ─────────────────────────────────────────────────────────────────

@app.post("/character", response_model=CharacterID, tags=["Characters"])
async def create_character(character: CharacterBase):
    return createCharacter(character)


@app.get("/character", response_model=list[CharacterID], tags=["Characters"])
async def show_characters():
    return showCharacters()


@app.get("/character/filter/class", response_model=list[CharacterID], tags=["Characters"])
async def filter_characters(character_class: str):
    return filterCharactersByClass(character_class)


@app.get("/character/search/name", response_model=CharacterID, tags=["Characters"])
async def search_character(name: str):
    character = searchCharacterByName(name)
    if not character:
        raise HTTPException(status_code=404, detail=f"Character '{name}' not found")
    return character


@app.get("/character/{id}", response_model=CharacterID, tags=["Characters"])
async def show_character(id: int):
    character = findCharacter(id)
    if not character:
        raise HTTPException(status_code=404, detail=f"{id} Character not found")
    return character


@app.patch("/character/{id}", response_model=CharacterID, tags=["Characters"])
async def update_character(id: int, character: CharacterUpdate):
    updated = updateCharacter(id, character)
    if not updated:
        raise HTTPException(status_code=404, detail=f"{id} Character not found")
    return updated


@app.delete("/character/{id}", response_model=CharacterID, tags=["Characters"])
async def delete_character(id: int):
    deleted = deleteCharacter(id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"{id} Character not found")
    return deleted


# ── WEAPON ────────────────────────────────────────────────────────────────────

@app.post("/weapon", response_model=WeaponID, tags=["Weapons"])
async def create_weapon(weapon: WeaponBase):
    return createWeapon(weapon)


@app.get("/weapon", response_model=list[WeaponID], tags=["Weapons"])
async def show_weapons():
    return showWeapons()


@app.get("/weapon/filter/type", response_model=list[WeaponID], tags=["Weapons"])
async def filter_weapons(weapon_type: str):
    return filterWeaponsByType(weapon_type)


@app.get("/weapon/search/name", response_model=WeaponID, tags=["Weapons"])
async def search_weapon(name: str):
    weapon = searchWeaponByName(name)
    if not weapon:
        raise HTTPException(status_code=404, detail=f"Weapon '{name}' not found")
    return weapon


@app.get("/weapon/{id}", response_model=WeaponID, tags=["Weapons"])
async def show_weapon(id: int):
    weapon = findWeapon(id)
    if not weapon:
        raise HTTPException(status_code=404, detail=f"{id} Weapon not found")
    return weapon


@app.patch("/weapon/{id}", response_model=WeaponID, tags=["Weapons"])
async def update_weapon(id: int, weapon: WeaponUpdate):
    updated = updateWeapon(id, weapon)
    if not updated:
        raise HTTPException(status_code=404, detail=f"{id} Weapon not found")
    return updated


@app.delete("/weapon/{id}", response_model=WeaponID, tags=["Weapons"])
async def delete_weapon(id: int):
    deleted = deleteWeapon(id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"{id} Weapon not found")
    return deleted


# ── BUILD ─────────────────────────────────────────────────────────────────────

@app.post("/build", response_model=BuildID, tags=["Builds"])
async def create_build(build: BuildBase):
    if not findCharacter(build.character_id):
        raise HTTPException(status_code=404, detail=f"Character {build.character_id} not found")
    if not findWeapon(build.weapon_id):
        raise HTTPException(status_code=404, detail=f"Weapon {build.weapon_id} not found")
    return createBuild(build)


@app.get("/build", response_model=list[BuildDetail], tags=["Builds"])
async def show_builds():
    return showBuildsDetail()


@app.get("/build/filter/focus", response_model=list[BuildID], tags=["Builds"])
async def filter_builds(focus: str):
    return filterBuildsByFocus(focus)


@app.get("/build/{id}", response_model=BuildDetail, tags=["Builds"])
async def show_build(id: int):
    build = findBuildDetail(id)
    if not build:
        raise HTTPException(status_code=404, detail=f"{id} Build not found")
    return build


@app.patch("/build/{id}", response_model=BuildID, tags=["Builds"])
async def update_build(id: int, build: BuildUpdate):
    updated = updateBuild(id, build)
    if not updated:
        raise HTTPException(status_code=404, detail=f"{id} Build not found")
    return updated


@app.delete("/build/{id}", response_model=BuildID, tags=["Builds"])
async def delete_build(id: int):
    deleted = deleteBuild(id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"{id} Build not found")
    return deleted