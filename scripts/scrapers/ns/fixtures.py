import re
from scrape_utils import parse_date, parse_time
from .exclusions import excluded_leagues, excluded_teams

def extract_club_id(a_tag):
    """Extract clubprofile ID from anchor tag href."""
    match = re.search(r"/clubprofile/(\d+)/", a_tag["href"])
    return match.group(1) if match else ""

def scrape(soups_by_league_id, team_id_map):
    matches = []

    for league_id, soup in soups_by_league_id.items():
        if league_id in excluded_leagues:
            continue

        for ul in soup.find_all("ul", class_=f"fixtures-{league_id}"):
            date = ul.get("data-date", "").strip()
            time = ul.get("data-time", "").strip()
            venue = ul.get("data-venue", "").strip()

            if date == "TBC" or time == "TBC":
                continue

            home_tag = ul.find("li", class_="fteam1").find("a")
            away_tag = ul.find("li", class_="fteam2").find("a")
            home_id = extract_club_id(home_tag)
            away_id = extract_club_id(away_tag)

            if not home_id or not away_id:
                continue

            if home_id in excluded_teams or away_id in excluded_teams:
                continue

            matches.append({
                "league_id": league_id,
                "home_id": home_id,
                "away_id": away_id,
                "date": parse_date(date),
                "time": parse_time(time),
                "venue": venue,
            })

    return matches
