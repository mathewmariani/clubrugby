import re
from scrape_utils import parse_date, parse_time

def extract_club_id(a_tag):
    """Extract clubprofile ID from anchor tag href."""
    match = re.search(r"/clubprofile/(\d+)/", a_tag["href"])
    return match.group(1) if match else ""

def scrape(soups_by_league, team_id_map=None):
    fixtures = []

    for league_id, soup in soups_by_league.items():
        for ul in soup.find_all("ul", class_="column-six table-body fixtures"):
            try:
                # Extract raw fields from data attributes
                date = ul.get("data-date", "").strip()
                time = ul.get("data-time", "").strip()
                home_tag = ul.find("li", class_="fteam1").find("a")
                away_tag = ul.find("li", class_="fteam2").find("a")
                home_id = extract_club_id(home_tag)
                away_id = extract_club_id(away_tag)

                # Build fixture
                fixtures.append({
                    "league_id": league_id,
                    "date": parse_date(date),
                    "time": parse_time(time),
                    "home_id": home_id,
                    "away_id": away_id,
                    "venue": ul.get("data-venue", "").strip(),
                })

                print(f"📅 Fixture: {home_id} vs {away_id} on {date} at {time}")

            except Exception as e:
                print(f"❌ Failed to parse fixture in league {league_id}: {e}")

    return fixtures
