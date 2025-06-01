import csv

def load_clubs(path="data/"):
    print("📖 Loading club list from clubs.csv...")
    with open(f"{path}/clubs.csv", newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def load_team_id_map(path="data/"):
    print("📖 Loading clubs.csv for team IDs...")
    team_id_map = {}
    with open(f"{path}/clubs.csv", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            team_id_map[row["name"].strip()] = row["id"].strip()
    return team_id_map

def load_league_ids(path="data/"):
    print("📖 Loading leagues.csv for league IDs...")
    league_ids = []
    with open(f"{path}/leagues.csv", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            league_ids.append(row["id"].strip())
    return league_ids
