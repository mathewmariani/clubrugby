import csv
from scrape_utils import get_soup, save_rows_to_csv

# Load team name-to-ID mapping
print("📖 Loading clubs.csv for team IDs...")
team_id_map = {}
with open("data/clubs.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        team_id_map[row["name"].strip()] = row["id"].strip()

# Load league IDs from CSV
print("📖 Loading leagues.csv for league IDs...")
league_ids = []
with open("data/leagues.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        league_ids.append(row["id"].strip())

base_url = "https://rugbyquebec.org/league/{}/"
matches = []

for league_id in league_ids:
    url = base_url.format(league_id)
    try:
        soup = get_soup(url)
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        continue

    for match in soup.find_all("ul", class_="column-seven table-body"):
        home_team = match.get("data-hometeam", "").strip()
        away_team = match.get("data-awayteam", "").strip()
        date = match.get("data-date", "").strip()
        time = match.get("data-time", "").strip()
        venue = match.get("data-venue", "").strip()

        matches.append([
            league_id,
            team_id_map.get(home_team, "UNKNOWN"),
            team_id_map.get(away_team, "UNKNOWN"),
            date, time, venue
        ])
        print(f"✅ Match: {home_team} vs {away_team} on {date} at {time} in {venue}")

save_rows_to_csv(
    "data/matches.csv",
    ["league_id", "home_id", "away_id", "date", "time", "venue"],
    matches
)