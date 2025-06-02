import re
from scrape_utils import parse_date, parse_time
from .exclusions import excluded_leagues, excluded_teams

def extract_club_id(a_tag):
    """Extract clubprofile ID from anchor tag href."""
    match = re.search(r"/clubprofile/(\d+)/", a_tag["href"])
    return match.group(1) if match else ""

def scrape(soups_by_league_id, team_id_map):
    results = []

    for league_id, soup in soups_by_league_id.items():
        if league_id in excluded_leagues:
            continue

        for ul in soup.find_all("ul", class_="results"):
            date = ul.get("data-date", "").strip()
            time = ul.get("data-time", "").strip()
            home_score = ul.get("data-homescore", "").strip()
            away_score = ul.get("data-awayscore", "").strip()

            home_tag = ul.find("li", class_="rteam1").find("a")
            away_tag = ul.find("li", class_="rteam2").find("a")
            home_id = extract_club_id(home_tag)
            away_id = extract_club_id(away_tag)

            if not home_id or not away_id:
                continue

            if home_id in excluded_teams or away_id in excluded_teams:
                continue

            results.append({
                "league_id": league_id,
                "date": parse_date(date),
                "time": parse_time(time),
                "home_id": home_id,
                "home_score": home_score,
                "away_id": away_id,
                "away_score": away_score,
            })

    return results
