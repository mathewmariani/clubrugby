import csv
from pathlib import Path

def load_clubs(base_path="data"):
    """
    Load clubs.csv from the given base_path (e.g. 'data/rugbyquebec')
    Returns a list of dicts.
    """
    clubs_file = Path(base_path) / "clubs.csv"
    print(f"📖 Loading club list from {clubs_file}...")
    with open(clubs_file, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def load_team_id_map(base_path="data"):
    """
    Load a map {club_name: club_id} from clubs.csv in base_path
    """
    clubs_file = Path(base_path) / "clubs.csv"
    print(f"📖 Loading team ID map from {clubs_file}...")
    team_id_map = {}
    with open(clubs_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            team_id_map[row["name"].strip()] = row["id"].strip()
    return team_id_map

def load_league_ids(base_path="data"):
    """
    Load a list of league IDs from leagues.csv in base_path
    """
    leagues_file = Path(base_path) / "leagues.csv"
    print(f"📖 Loading league IDs from {leagues_file}...")
    league_ids = []
    with open(leagues_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            league_ids.append(row["id"].strip())
    return league_ids
