from pydantic import BaseModel, Field
class models.weapon_types import  WeaponType

class WeaponBase(BaseModel):
    name:      str | None = Field(default=None, min_length=2, max_length=64)
    weapon_type      WeaponType | None = Field(default=None)
    damage:        int | None = Field(default=None, gt=0, )
    scaling: str | None = Field(default=None, min_length=1, max_length=32)

class WeaponID(WeaponBase):
    id: int | None = Field(default=None, gt=0)

class WeaponUpdate(WeaponBase):
    pass