from league_utils import load_team_id_map, load_league_ids
from scrape_utils import get_soup, save_rows_to_csv

def scrape_standings(save_path="data/", save=True):
    team_id_map = load_team_id_map(save_path)
    league_ids = load_league_ids(save_path)
    base_url = "https://rugbyquebec.org/league/{}/"
    standings_data = []

    for league_id in league_ids:
        url = base_url.format(league_id)
        try:
            soup = get_soup(url)
        except Exception as e:
            print(f"❌ Failed to fetch {url}: {e}")
            continue

        position = 1
        for row in soup.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) >= 13:
                team_name = cells[1].get_text(strip=True)
                team_id = team_id_map.get(team_name, "UNKNOWN")
                standings_data.append([
                    league_id,
                    team_id,
                    position,  # pos
                    cells[2].get_text(strip=True),  # gp
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
                position += 1

    if save:
        save_rows_to_csv(
            f"{save_path}/standings.csv",
            [
                "league_id", "team_id", "pos", "gp", "w", "d", "l",
                "pf", "pa", "diff", "tf", "ta", "td", "pts"
            ],
            standings_data
        )
        print("🎉 Standings scraping complete!")

    return standings_data

if __name__ == "__main__":
    scrape_standings()
