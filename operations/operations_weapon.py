from models import *
from operations.operations_csv import (
    WEAPONS_CSV, WEAPONS_COLS,
    newID, read_active_rows, read_all_rows, write_rows, strip_active
)


def createWeapon(weapon: WeaponBase) -> WeaponID:
    new_id = newID(WEAPONS_CSV)
    new_wpn = WeaponID(id=new_id, **weapon.model_dump())
    row = new_wpn.model_dump(mode="json")
    row["active"] = "True"
    all_rows = read_all_rows(WEAPONS_CSV, WEAPONS_COLS)
    all_rows.append(row)
    write_rows(WEAPONS_CSV, WEAPONS_COLS, all_rows)
    return new_wpn


def showWeapons() -> list[WeaponID]:
    return [WeaponID(**strip_active(row)) for row in read_active_rows(WEAPONS_CSV, WEAPONS_COLS)]


def findWeapon(id: int) -> Optional[WeaponID]:
    for row in read_active_rows(WEAPONS_CSV, WEAPONS_COLS):
        if int(row["id"]) == id:
            return WeaponID(**strip_active(row))
    return None


def filterWeaponsByType(weapon_type: str) -> list[WeaponID]:
    return [w for w in showWeapons() if w.weapon_type == weapon_type]


def searchWeaponByName(name: str) -> Optional[WeaponID]:
    for wpn in showWeapons():
        if wpn.name and wpn.name.lower() == name.lower():
            return wpn
    return None


def updateWeapon(id: int, data: WeaponUpdate) -> Optional[WeaponID]:
    all_rows = read_all_rows(WEAPONS_CSV, WEAPONS_COLS)
    updated = None
    for row in all_rows:
        if int(row["id"]) == id and row.get("active") == "True":
            row.update({k: v for k, v in data.model_dump(mode="json", exclude_unset=True).items()})
            updated = WeaponID(**strip_active(row))
    if updated:
        write_rows(WEAPONS_CSV, WEAPONS_COLS, all_rows)
    return updated


def deleteWeapon(id: int) -> Optional[WeaponID]:
    all_rows = read_all_rows(WEAPONS_CSV, WEAPONS_COLS)
    deleted = None
    for row in all_rows:
        if int(row["id"]) == id and row.get("active") == "True":
            row["active"] = "False"
            deleted = WeaponID(**strip_active(row))
    if deleted:
        write_rows(WEAPONS_CSV, WEAPONS_COLS, all_rows)
    return deleted