from models import *
from operations.operations_csv import (
    CHARACTERS_CSV, CHARACTERS_COLS,
    newID, read_active_rows, read_all_rows, write_rows, strip_active
)




def createCharacter(character: CharacterBase) -> CharacterID:
    new_id = newID(CHARACTERS_CSV)
    new_char = CharacterID(id=new_id, **character.model_dump())
    row = new_char.model_dump(mode="json")
    row["active"] = "True"
    all_rows = read_all_rows(CHARACTERS_CSV, CHARACTERS_COLS)
    all_rows.append(row)
    write_rows(CHARACTERS_CSV, CHARACTERS_COLS, all_rows)
    return new_char


def showCharacters() -> list[CharacterID]:
    return [CharacterID(**strip_active(row)) for row in read_active_rows(CHARACTERS_CSV, CHARACTERS_COLS)]


def findCharacter(id: int) -> Optional[CharacterID]:
    for row in read_active_rows(CHARACTERS_CSV, CHARACTERS_COLS):
        if int(row["id"]) == id:
            return CharacterID(**strip_active(row))
    return None


def filterCharactersByClass(character_class: str) -> list[CharacterID]:

    valid_classes = [c.value for c in CharacterClass]
    if character_class.lower() not in valid_classes:
        return None
    return [c for c in showCharacters() if c.character_class == character_class.lower()]


def searchCharacterByName(name: str) -> Optional[CharacterID]:
    for char in showCharacters():
        if char.name and char.name.lower() == name.lower():
            return char
    return None


def updateCharacter(id: int, data: CharacterUpdate) -> Optional[CharacterID]:
    all_rows = read_all_rows(CHARACTERS_CSV, CHARACTERS_COLS)
    updated = None
    for row in all_rows:
        if int(row["id"]) == id and row.get("active") == "True":
            row.update({k: v for k, v in data.model_dump(mode="json", exclude_unset=True).items()})
            updated = CharacterID(**strip_active(row))
    if updated:
        write_rows(CHARACTERS_CSV, CHARACTERS_COLS, all_rows)
    return updated


def deleteCharacter(id: int) -> Optional[CharacterID]:
    all_rows = read_all_rows(CHARACTERS_CSV, CHARACTERS_COLS)
    deleted = None
    for row in all_rows:
        if int(row["id"]) == id and row.get("active") == "True":
            row["active"] = "False"
            deleted = CharacterID(**strip_active(row))
    if deleted:
        write_rows(CHARACTERS_CSV, CHARACTERS_COLS, all_rows)
    return deletedx