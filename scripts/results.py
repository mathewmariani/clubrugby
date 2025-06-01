from league_utils import load_team_id_map, load_league_ids
from scrape_utils import get_soup, save_rows_to_csv

def scrape_results(save_path="data/", save=True):
    team_id_map = load_team_id_map(save_path)
    league_ids = load_league_ids(save_path)
    base_url = "https://rugbyquebec.org/league/{}/"
    results = []

    for league_id in league_ids:
        url = base_url.format(league_id)
        try:
            soup = get_soup(url)
        except Exception as e:
            print(f"❌ Failed to fetch {url}: {e}")
            continue

        for match in soup.find_all("ul", class_="column-six table-body resul"):
            date = match.get("data-date", "").strip()
            time = match.get("data-time", "").strip()
            home_team = match.get("data-hometeam", "").strip()
            away_team = match.get("data-awayteam", "").strip()

            home_score_tag = match.find("span", class_="score-value fir")
            away_score_tag = match.find("span", class_="score-value sec")

            home_score = home_score_tag.get_text(strip=True) if home_score_tag else ""
            away_score = away_score_tag.get_text(strip=True) if away_score_tag else ""

            results.append([
                league_id, date, time,
                team_id_map.get(home_team, "UNKNOWN"),
                home_score,
                team_id_map.get(away_team, "UNKNOWN"),
                away_score
            ])
            print(f"✅ Result: {home_team} {home_score} - {away_score} {away_team} on {date} at {time}")

    if save:
        save_rows_to_csv(
            f"{save_path}/results.csv",
            ["league_id", "date", "time", "home_id", "home_score", "away_id", "away_score"],
            results
        )
        print("🎉 Results scraping complete!")

    return results

if __name__ == "__main__":
    scrape_results()
