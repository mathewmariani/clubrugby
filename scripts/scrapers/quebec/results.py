def scrape(soups_by_league_id, team_id_map):
    results = []

    for league_id, soup in soups_by_league_id.items():
        for match in soup.find_all("ul", class_="column-six table-body resul"):
            date = match.get("data-date", "").strip()
            time = match.get("data-time", "").strip()
            home_team = match.get("data-hometeam", "").strip()
            away_team = match.get("data-awayteam", "").strip()

            home_score_tag = match.find("span", class_="score-value fir")
            away_score_tag = match.find("span", class_="score-value sec")

            home_score = home_score_tag.get_text(strip=True) if home_score_tag else ""
            away_score = away_score_tag.get_text(strip=True) if away_score_tag else ""

            results.append({
                "league_id": league_id,
                "date": date,
                "time": time,
                "home_id": team_id_map.get(home_team, "UNKNOWN"),
                "home_score": home_score,
                "away_id": team_id_map.get(away_team, "UNKNOWN"),
                "away_score": away_score,
            })

            print(f"✅ Result: {home_team} {home_score} - {away_score} {away_team} on {date} at {time}")

    return results
