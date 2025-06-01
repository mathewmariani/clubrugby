def scrape(soups_by_league_id, team_id_map):
    matches = []

    for league_id, soup in soups_by_league_id.items():
        for match in soup.find_all("ul", class_="column-seven table-body"):
            home_team = match.get("data-hometeam", "").strip()
            away_team = match.get("data-awayteam", "").strip()
            date = match.get("data-date", "").strip()
            time = match.get("data-time", "").strip()
            venue = match.get("data-venue", "").strip()

            matches.append({
                "league_id": league_id,
                "home_id": team_id_map.get(home_team, "UNKNOWN"),
                "away_id": team_id_map.get(away_team, "UNKNOWN"),
                "date": date,
                "time": time,
                "venue": venue,
            })

            print(f"✅ Match: {home_team} vs {away_team} on {date} at {time} in {venue}")

    return matches

