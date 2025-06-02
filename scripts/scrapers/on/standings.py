import re
from .exclusions import excluded_leagues, excluded_teams

def extract_club_id(a_tag):
    """Extract clubprofile ID from anchor tag href."""
    match = re.search(r"/clubprofile/(\d+)/", a_tag["href"])
    return match.group(1) if match else ""

def find_team_id_by_name(name, team_map):
    for canonical_name in team_map:
        if name.startswith(canonical_name):
            return team_map[canonical_name]
    return None

def scrape(soups_by_league, team_id_map):
    standings_data = []

    for league_id, soup in soups_by_league.items():
        if league_id in excluded_leagues:
            continue

        position = 1
        for row in soup.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) >= 13:
                team_name = cells[1].get_text(strip=True)
                team_id = find_team_id_by_name(team_name, team_id_map)

                if not team_id or team_id in excluded_teams:
                    continue

                standings_data.append({
                    "league_id": league_id,
                    "team_id": team_id,
                    "pos": position,
                    "gp": cells[2].get_text(strip=True),
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
