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
    return show_characters()

@app.post("/character", response_model=list[CharacterID], tags=["Character"])
async def create_character(character:CharacterBase):
    return create_character(character)

models finished gotta keep movin up with the endpoints