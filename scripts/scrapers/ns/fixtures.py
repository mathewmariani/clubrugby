import re
from scrape_utils import parse_date, parse_time

def extract_club_id(a_tag):
    """Extract clubprofile ID from anchor tag href."""
    match = re.search(r"/clubprofile/(\d+)/", a_tag["href"])
    return match.group(1) if match else ""

def scrape(soups_by_league_id, team_id_map):
    matches = []

    for league_id, soup in soups_by_league_id.items():
        for ul in soup.find_all("ul", class_=f"fixtures-{league_id}"):
            # get match data
            date = ul.get("data-date", "").strip()
            time = ul.get("data-time", "").strip()
            venue = ul.get("data-venue", "").strip()

            if date == "TBC" or time == "TBC":
                continue

            # get team info
            home_tag = ul.find("li", class_="fteam1").find("a")
            away_tag = ul.find("li", class_="fteam2").find("a")
            home_id = extract_club_id(home_tag)
            away_id = extract_club_id(away_tag)

            matches.append({
                "league_id": league_id,
                "home_id": home_id,
                "away_id": away_id,
                "date": parse_date(date),
                "time": parse_time(time),
                "venue": venue,
            })

            # print(f"✅ Match: {home_id} vs {away_id} on {date} at {time} in {venue}")

    return matches

