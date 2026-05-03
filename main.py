from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Elden Ring  API",
    description="Elden Ring build manager API",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {"message": "Elden Ring Build API"}



# ── CHARACTER ─────────────────────────────────────────────────────────────────
@app.get("/character", response_model=list[CharacterID], tags=["Character"])
async def show_characters():
    return showCharacters()

@app.post("/character", response_model=list[CharacterID], tags=["Character"])
async def create_character(character:CharacterBase):
    return createCharacter(character)

@app.get("/character/filter/class", response_model=list[CharacterID], tags=["Character"])
async def filter_characters(characters_class: str):
    return filterCharacters(characters_class)
