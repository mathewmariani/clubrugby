from league_utils import load_team_id_map, load_league_ids
from scrape_utils import get_soup, save_rows_to_csv

def scrape_fixtures(save_path="data/", save=True):
    team_id_map = load_team_id_map(save_path)
    league_ids = load_league_ids(save_path)

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

    if save:
        save_rows_to_csv(
            f"{save_path}/fixtures.csv",
            ["league_id", "home_id", "away_id", "date", "time", "venue"],
            matches
        )
        print("🎉 Fixture scraping complete!")

    return matches

if __name__ == "__main__":
    scrape_fixtures()
