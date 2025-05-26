import csv
from datetime import datetime
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
standings_data = []

for league_id in league_ids:
    url = base_url.format(league_id)
    try:
        soup = get_soup(url)
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        continue

    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) >= 13:
            team_name = cells[1].get_text(strip=True)
            team_id = team_id_map.get(team_name, "UNKNOWN")

            standings_data.append([
                league_id,
                team_id,
                cells[0].get_text(strip=True),  # pos
                cells[2].get_text(strip=True),  # pld
                cells[3].get_text(strip=True),  # w
                cells[4].get_text(strip=True),  # d
                cells[5].get_text(strip=True),  # l
                cells[6].get_text(strip=True),  # pf
                cells[7].get_text(strip=True),  # pa
                cells[8].get_text(strip=True),  # diff
                cells[9].get_text(strip=True),  # tf
                cells[10].get_text(strip=True), # ta
                cells[11].get_text(strip=True), # td
                cells[12].get_text(strip=True), # pts
            ])
            print(f"✅ Added: {team_name} from league {league_id}")

save_rows_to_csv(
    "data/standings.csv",
    [
        "league_id", "team_id", "pos", "pld", "w", "d", "l",
        "pf", "pa", "diff", "tf", "ta", "td", "pts"
    ],
    standings_data
)