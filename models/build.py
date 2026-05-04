from pydantic import BaseModel, Field

class BuildBase(BaseModel):
    character_id: int | None = Field(default=None, gt=0)
    weapon_id: int | None = Field(default=None, gt=0)
    focus: str | None = Field(default=None, min_length=2, max_length=64)
    notes: str | None = Field(default="")

class BuildID(BuildBase):
    id: int | None = Field(default=None, gt=0)

class BuildUpdate(BuildBase):
    pass
