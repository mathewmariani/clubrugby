import re

def extract_team_id(a_tag):
    """Extract team_id from anchor tag."""
    match = re.search(r"team_id=(\d+)", a_tag["href"])
    return match.group(1) if match else ""

def scrape(soups_by_league, team_id_map=None):
    results = []

    for league_id, soup in soups_by_league.items():
        for ul in soup.find_all("ul", class_="column-six table-body"):
            try:
                date = ul.find("li", class_="ftime").get_text(strip=True)
                time = ul.find_all("li")[1].get_text(strip=True)

                home_tag = ul.find("li", class_="fteam1").find("a")
                away_tag = ul.find("li", class_="fteam2").find("a")
                home_id = extract_team_id(home_tag)
                away_id = extract_team_id(away_tag)

                vs_result = ul.find("span", class_="vs-result")
                home_score = vs_result.find("span", class_="homeScore").get_text(strip=True)
                away_score = vs_result.find("span", class_="awayScore").get_text(strip=True)

                results.append({
                    "league_id": league_id,
                    "date": date,
                    "time": time,
                    "home_id": team_id_map.get(home_id, home_id) if team_id_map else home_id,
                    "home_score": home_score,
                    "away_id": team_id_map.get(away_id, away_id) if team_id_map else away_id,
                    "away_score": away_score,
                })

                print(f"✅ Result: {home_id} {home_score} - {away_score} {away_id} on {date} at {time}")

            except Exception as e:
                print(f"❌ Failed to parse result in league {league_id}: {e}")

    return results
