# scrapers/quebec/standings.py

def scrape(soups_by_league, team_id_map):
    standings_data = []

    for league_id, soup in soups_by_league.items():
        position = 1
        for row in soup.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) >= 13:
                team_name = cells[1].get_text(strip=True)
                team_id = team_id_map.get(team_name, "UNKNOWN")
                standings_data.append({
                    "league_id": league_id,
                    "team_id": team_id,
                    "pos": position,
                    "pld": cells[2].get_text(strip=True),
                    "w": cells[3].get_text(strip=True),
                    "d": cells[4].get_text(strip=True),
                    "l": cells[5].get_text(strip=True),
                    "pf": cells[6].get_text(strip=True),
                    "pa": cells[7].get_text(strip=True),
                    "diff": cells[8].get_text(strip=True),
                    "tf": cells[9].get_text(strip=True),
                    "ta": cells[10].get_text(strip=True),
                    "td": cells[11].get_text(strip=True),
                    "pts": cells[12].get_text(strip=True),
                })
                position += 1

    return standings_data
