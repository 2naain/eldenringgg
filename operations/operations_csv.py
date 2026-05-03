import csv
import os

CSV_DIR = "data"

CHARACTERS_CSV = os.path.join(CSV_DIR, "characters.csv")
WEAPONS_CSV    = os.path.join(CSV_DIR, "weapons.csv")
BUILDS_CSV     = os.path.join(CSV_DIR, "builds.csv")

CHARACTERS_COLS = ["id", "name", "character_class", "level", "game", "active"]
WEAPONS_COLS    = ["id", "name", "weapon_type", "damage", "scaling", "active"]
BUILDS_COLS     = ["id", "character_id", "weapon_id", "focus", "notes", "active"]


def newID(csv_file: str) -> int:
    try:
        with open(csv_file, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            ids = [int(row["id"]) for row in reader]
            return max(ids) + 1 if ids else 1
    except (FileNotFoundError, csv.Error, ValueError):
        return 1


def ensure_file(csv_file: str, columns: list):
    if not os.path.exists(csv_file):
        with open(csv_file, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()


def read_active_rows(csv_file: str, columns: list) -> list[dict]:
    ensure_file(csv_file, columns)
    with open(csv_file, newline="") as file:
        reader = csv.DictReader(file)
        return [row for row in reader if row.get("active", "True") == "True"]


def read_all_rows(csv_file: str, columns: list) -> list[dict]:
    ensure_file(csv_file, columns)
    with open(csv_file, newline="") as file:
        return list(csv.DictReader(file))


def write_rows(csv_file: str, columns: list, rows: list[dict]):
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def strip_active(row: dict) -> dict:
    return {k: v for k, v in row.items() if k != "active"}
