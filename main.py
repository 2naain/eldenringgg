from fastapi import FastAPI, HTTPException

from models import CharacterUpdate

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
