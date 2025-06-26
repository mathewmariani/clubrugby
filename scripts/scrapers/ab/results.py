import re
from .exclusions import excluded_leagues, excluded_teams, club_refs
from scrape_utils import parse_date, parse_time

def extract_club_id(a_tag):
    """Extract clubprofile ID from anchor tag href."""
    match = re.search(r"/clubprofile/(\d+)/", a_tag["href"])
    return match.group(1) if match else ""

def clean_score(score_str):
    return re.sub(r"\s*\(\s*\d*\s*\)", "", score_str)

def scrape(soups_by_league, team_id_map=None):
    results = []

    for league_id, soup in soups_by_league.items():
        if league_id in excluded_leagues:
            continue

        for ul in soup.find_all("ul", class_="column-six table-body"):
            try:
                date = ul.find("li", class_="ftime").get_text(strip=True)
                time = ul.find_all("li")[1].get_text(strip=True)

                home_tag = ul.find("li", class_="fteam1").find("a")
                away_tag = ul.find("li", class_="fteam2").find("a")
                home_id = extract_club_id(home_tag)
                away_id = extract_club_id(away_tag)

                vs_result = ul.find("span", class_="vs-result")
                home_score_raw = vs_result.find("span", class_="homeScore").get_text(strip=True)
                away_score_raw = vs_result.find("span", class_="awayScore").get_text(strip=True)

                # Clean scores by removing " (digit)"
                home_score = clean_score(home_score_raw)
                away_score = clean_score(away_score_raw)

                # Normalize using club_refs
                home_id = club_refs.get(home_id, home_id)
                away_id = club_refs.get(away_id, away_id)

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

            except Exception as e:
                print(f"❌ Failed to parse result in league {league_id}: {e}")

    return results
