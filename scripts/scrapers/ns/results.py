import re
from scrape_utils import parse_date, parse_time

def extract_club_id(a_tag):
    """Extract clubprofile ID from anchor tag href."""
    match = re.search(r"/clubprofile/(\d+)/", a_tag["href"])
    return match.group(1) if match else ""

def scrape(soups_by_league_id, team_id_map):
    results = []

    for league_id, soup in soups_by_league_id.items():
        for ul in soup.find_all("ul", class_="results"):
            # get match data
            date = ul.get("data-date", "").strip()
            time = ul.get("data-time", "").strip()
            home_score = ul.get("data-homescore", "").strip()
            away_score = ul.get("data-awayscore", "").strip()

            # get team info
            home_tag = ul.find("li", class_="rteam1").find("a")
            away_tag = ul.find("li", class_="rteam2").find("a")
            home_id = extract_club_id(home_tag)
            away_id = extract_club_id(away_tag)

            results.append({
                "league_id": league_id,
                "date": parse_date(date),
                "time": parse_time(time),
                "home_id": home_id,
                "home_score": home_score,
                "away_id": away_id,
                "away_score": away_score,
            })

            # print(f"✅ Result: {home_team} {home_score} - {away_score} {away_team} on {date} at {time}")

    return results
