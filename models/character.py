from pydantic import BaseModel, Field

class CharacterID(BaseModel):
    name:  str | None = Field(default= None, min_length=2, max_length=64)
    character_class: CharacterClass | None = Field(default=None)
    level: int  | None = Field(default=None, gt=0, le=713)
    game: str | None = Field(default="Elden Ring")

class CharacterID(CharacterBase):
    id: int | None = Field(default=None, gt=0)

class CharacterUpdate(CharacterBase):
        pass