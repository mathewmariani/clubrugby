import re
from scrape_utils import parse_date, parse_time
from .exclusions import excluded_leagues, excluded_teams, club_refs

def extract_club_id(a_tag):
    """Extract clubprofile ID from anchor tag href."""
    match = re.search(r"/clubprofile/(\d+)/", a_tag["href"])
    return match.group(1) if match else ""

def scrape(soups_by_league, team_id_map=None):
    fixtures = []

    for league_id, soup in soups_by_league.items():
        if league_id in excluded_leagues:
            continue

        for ul in soup.find_all("ul", class_="column-six table-body fixtures"):
            try:
                # Extract raw fields from data attributes
                date = ul.get("data-date", "").strip()
                time = ul.get("data-time", "").strip()
                home_tag = ul.find("li", class_="fteam1").find("a")
                away_tag = ul.find("li", class_="fteam2").find("a")
                home_id = extract_club_id(home_tag)
                away_id = extract_club_id(away_tag)

                # Normalize using club_refs
                home_id = club_refs.get(home_id, home_id)
                away_id = club_refs.get(away_id, away_id)

                if not home_id or not away_id:
                    continue

                if home_id in excluded_teams or away_id in excluded_teams:
                    continue

                # Build fixture
                fixtures.append({
                    "league_id": league_id,
                    "date": parse_date(date),
                    "time": parse_time(time),
                    "home_id": home_id,
                    "away_id": away_id,
                    "venue": ul.get("data-venue", "").strip(),
                })

                # print(f"📅 Fixture: {home_id} vs {away_id} on {date} at {time}")

            except Exception as e:
                print(f"❌ Failed to parse fixture in league {league_id}: {e}")

    return fixtures
