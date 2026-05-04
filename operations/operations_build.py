from models import *
from operations.operations_csv import (
    BUILDS_CSV, BUILDS_COLS,
    newID, read_active_rows, read_all_rows, write_rows, strip_active
)


def createBuild(build: BuildBase) -> BuildID:
    new_id = newID(BUILDS_CSV)
    new_build = BuildID(id=new_id, **build.model_dump())
    row = new_build.model_dump(mode="json")
    row["active"] = "True"
    all_rows = read_all_rows(BUILDS_CSV, BUILDS_COLS)
    all_rows.append(row)
    write_rows(BUILDS_CSV, BUILDS_COLS, all_rows)
    return new_build


def showBuilds() -> list[BuildID]:
    return [BuildID(**strip_active(row)) for row in read_active_rows(BUILDS_CSV, BUILDS_COLS)]


def findBuild(id: int) -> Optional[BuildID]:
    for row in read_active_rows(BUILDS_CSV, BUILDS_COLS):
        if int(row["id"]) == id:
            return BuildID(**strip_active(row))
    return None


def filterBuildsByFocus(focus: str) -> list[BuildID]:
    return [b for b in showBuilds() if b.focus.lower() == focus.lower()]


def updateBuild(id: int, data: BuildUpdate) -> Optional[BuildID]:
    all_rows = read_all_rows(BUILDS_CSV, BUILDS_COLS)
    updated = None
    for row in all_rows:
        if int(row["id"]) == id and row.get("active") == "True":
            row.update({k: v for k, v in data.model_dump(mode="json", exclude_unset=True).items()})
            updated = BuildID(**strip_active(row))
    if updated:
        write_rows(BUILDS_CSV, BUILDS_COLS, all_rows)
    return updated


def deleteBuild(id: int) -> Optional[BuildID]:
    all_rows = read_all_rows(BUILDS_CSV, BUILDS_COLS)
    deleted = None
    for row in all_rows:
        if int(row["id"]) == id and row.get("active") == "True":
            row["active"] = "False"
            deleted = BuildID(**strip_active(row))
    if deleted:
        write_rows(BUILDS_CSV, BUILDS_COLS, all_rows)
    return deleted
