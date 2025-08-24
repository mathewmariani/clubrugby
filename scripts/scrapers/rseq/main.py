import requests
import csv
import os

team_id_map = {
    # cegep
    "01c83f3e-efe3-4d3b-8864-5f79ac764329": "e4a5282d-4093-4c43-98ef-103912518fc9",
    "28daff3d-3fbc-4f00-9092-f87940c4232d": "22c1dc92-c684-4528-ac31-154ff5d0daaa",
    "d6627ecd-a2c7-4eb2-9255-1a2c9ea73840": "e635ab97-3ddf-47c6-8b1b-10aa0eb30679",
    "897495b8-1451-4510-8ce4-6038228aedca": "8d0be92f-fbe0-454b-a35f-a366282ecade",

    # university
    "78a948a7-5eed-4f98-ba32-1b73ba2b3e91": "a1044ae6-abd9-49db-9e69-9e94617cb64f",
    "2ecc0d44-bbe0-4b8f-84e3-777f76ccacfb": "990077e5-e3ef-49b3-82aa-dc1fea75388a",
    "7effe149-5b71-4664-bade-6f91c5516c74": "e539f8b7-945a-4a92-9e71-390c704b0571",
    "effba245-ab6c-4f22-9897-c32c8a2cd59f": "25a57eba-fc38-4481-9438-5e49fcb2c161",
    "559d4c83-3b88-489f-a343-62e84f44a5df": "7ee0ec36-4447-4803-83ef-822f3e32d7d0",
    "b4d1de6c-3279-4c62-979d-9b5eb47ebd40": "fc7a0121-93db-4711-8366-e8ac903a0986",
}

team_logo_map = {
    # cegep_m
    "01c83f3e-efe3-4d3b-8864-5f79ac764329": "https://rseq.ca/ImageGen.ashx?image=/media/24420/1.jpg&width=58&height=58&pad=true&constrain=true",
    "28daff3d-3fbc-4f00-9092-f87940c4232d": "https://rseq.ca/ImageGen.ashx?image=/media/2536015/2022-2023_dawson_blues-logo-full-color-rgb.jpg&width=58&height=58&pad=true&constrain=true",
    "6aacdf88-aad8-4e59-a052-1bb3ca919973": "https://rseq.ca/ImageGen.ashx?image=/media/463331/microsoftteams-image.png&width=58&height=58&pad=true&constrain=true",
    "d6627ecd-a2c7-4eb2-9255-1a2c9ea73840": "https://rseq.ca/ImageGen.ashx?image=/media/24490/john_abbott.jpg&width=58&height=58&pad=true&constrain=true",
    "897495b8-1451-4510-8ce4-6038228aedca": "https://rseq.ca/ImageGen.ashx?image=/media/24630/vaniercheetahsrgblrg__2_.gif&width=58&height=58&pad=true&constrain=true",

    # cegep_f
    "e4a5282d-4093-4c43-98ef-103912518fc9": "https://rseq.ca/ImageGen.ashx?image=/media/24420/1.jpg&width=58&height=58&pad=true&constrain=true",
    "22c1dc92-c684-4528-ac31-154ff5d0daaa": "https://rseq.ca/ImageGen.ashx?image=/media/2536015/2022-2023_dawson_blues-logo-full-color-rgb.jpg&width=58&height=58&pad=true&constrain=true",
    "e635ab97-3ddf-47c6-8b1b-10aa0eb30679": "https://rseq.ca/ImageGen.ashx?image=/media/24490/john_abbott.jpg&width=58&height=58&pad=true&constrain=true",
    "8d0be92f-fbe0-454b-a35f-a366282ecade": "https://rseq.ca/ImageGen.ashx?image=/media/24630/vaniercheetahsrgblrg__2_.gif&width=58&height=58&pad=true&constrain=true",

    # university_m
    "78a948a7-5eed-4f98-ba32-1b73ba2b3e91": "https://rseq.ca/ImageGen.ashx?image=/media/24646/uni_logos_bsh_gaiters.jpg&width=58&height=58&pad=true&constrain=true",
    "2ecc0d44-bbe0-4b8f-84e3-777f76ccacfb": "https://rseq.ca/ImageGen.ashx?image=/media/492927/uni_logos_car_ravens.jpg&width=58&height=58&pad=true&constrain=true",
    "7effe149-5b71-4664-bade-6f91c5516c74": "https://rseq.ca/ImageGen.ashx?image=/media/24651/uni_logos_cnd_stingers.jpg&width=58&height=58&pad=true&constrain=true",
    "1d966340-7fb7-4170-b623-f1b8305ed00a": "https://rseq.ca/ImageGen.ashx?image=/media/24656/logo_piranhas_ets-200x130.gif&width=58&height=58&pad=true&constrain=true",
    "effba245-ab6c-4f22-9897-c32c8a2cd59f": "https://rseq.ca/ImageGen.ashx?image=/media/76121/uni_logos_mcg.jpg&width=58&height=58&pad=true&constrain=true",
    "559d4c83-3b88-489f-a343-62e84f44a5df": "https://rseq.ca/ImageGen.ashx?image=/media/24671/uni_logos_mtl_carabins.jpg&width=58&height=58&pad=true&constrain=true",
    "b4d1de6c-3279-4c62-979d-9b5eb47ebd40": "https://rseq.ca/ImageGen.ashx?image=/media/492903/uni_logos_ott_geegees.jpg&width=58&height=58&pad=true&constrain=true",

    # university_f
    "a1044ae6-abd9-49db-9e69-9e94617cb64f": "https://rseq.ca/ImageGen.ashx?image=/media/24646/uni_logos_bsh_gaiters.jpg&width=58&height=58&pad=true&constrain=true",
    "990077e5-e3ef-49b3-82aa-dc1fea75388a": "https://rseq.ca/ImageGen.ashx?image=/media/492927/uni_logos_car_ravens.jpg&width=58&height=58&pad=true&constrain=true",
    "e539f8b7-945a-4a92-9e71-390c704b0571": "https://rseq.ca/ImageGen.ashx?image=/media/24651/uni_logos_cnd_stingers.jpg&width=58&height=58&pad=true&constrain=true",
    "0423d176-be40-4c29-8fb3-b6cb5927a207": "https://rseq.ca/ImageGen.ashx?image=/media/24661/uni_logos_lvl_rouge_or.jpg&width=58&height=58&pad=true&constrain=true",
    "25a57eba-fc38-4481-9438-5e49fcb2c161": "https://rseq.ca/ImageGen.ashx?image=/media/76121/uni_logos_mcg.jpg&width=58&height=58&pad=true&constrain=true",
    "7ee0ec36-4447-4803-83ef-822f3e32d7d0": "https://rseq.ca/ImageGen.ashx?image=/media/24671/uni_logos_mtl_carabins.jpg&width=58&height=58&pad=true&constrain=true",
    "fc7a0121-93db-4711-8366-e8ac903a0986": "https://rseq.ca/ImageGen.ashx?image=/media/492903/uni_logos_ott_geegees.jpg&width=58&height=58&pad=true&constrain=true",
    "c532d0d3-a9ce-440e-8256-9232f4d23713": "https://rseq.ca/ImageGen.ashx?image=/media/24676/uni_logos_she_vo.png&width=58&height=58&pad=true&constrain=true",
}

def id_to_logo(team_id):
    return team_logo_map.get(team_id, "")

# Map of leagues
leagues = {
    "cegep_m": "77390fac-c162-47e4-9f91-b4bf5151b938",
    "cegep_f": "a87e9fe1-3972-42eb-be01-b19f1304c3b4",
    "university_m": "c80803ae-8c87-4619-8d76-3eda0fdf2d27",
    "university_f": "f675b71f-ef1a-4dc5-ba09-0e378be48975",
}

url = "https://s1.rseq.ca/api/LeagueApi/GetLeagueDiffusion/"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "https://diffusion.rseq.ca",
    "Referer": "https://diffusion.rseq.ca/"
}

# Paths for CSV files
os.makedirs("data/rseq/2025", exist_ok=True)
teams_csv = "data/rseq/2025/clubs.csv"
fixtures_csv = "data/rseq/2025/fixtures.csv"
results_csv = "data/rseq/2025/results.csv"
standings_csv = "data/rseq/2025/standings.csv"

# Initialize CSV files with headers if they don't exist
# Clear CSV files and write headers
with open(teams_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "code", "pseudonym", "logo_url"], quoting=csv.QUOTE_ALL)
    writer.writeheader()

with open(fixtures_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["league_id","home_id","away_id","date","time","venue"], quoting=csv.QUOTE_ALL)
    writer.writeheader()

with open(results_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["league_id","date","time","home_id","home_score","away_id","away_score"], quoting=csv.QUOTE_ALL)
    writer.writeheader()

with open(standings_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["league_id","team_id","pos","pld","w","d","l","pf","pa","diff","tf","ta","td","pts"], quoting=csv.QUOTE_ALL)
    writer.writeheader()

def minutes_to_hhmm(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"


# Fetch each league and append to CSVs
for league_name, league_id in leagues.items():
    print(f"Fetching {league_name}...")
    response = requests.get(url, params={"leagueId": league_id}, headers=headers)
    response.raise_for_status()
    data = response.json()

    # Teams
    teams = data.get("Teams", [])
    with open(teams_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "code", "pseudonym", "logo_url"], quoting=csv.QUOTE_ALL)
        for team in teams:
            writer.writerow({
                "id": team.get("TeamId", ""),
                "name": team.get("TeamName", ""),
                "code": team.get("TeamCode", ""),
                "pseudonym": team.get("TeamPseudonym", ""),
                "logo_url": id_to_logo(team.get("TeamId", "")),
            })

    # Fixtures
    fixtures = data.get("RegularSeasonGames", [])
    with open(fixtures_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["league_id","home_id","away_id","date","time","venue"], quoting=csv.QUOTE_ALL)
        for fixture in fixtures:
            if fixture.get("IsSubmittedForStandings") is True:
                continue 
            writer.writerow({
                "league_id": fixture.get("LeagueId", ""),
                "home_id": fixture.get("HomeTeamId", ""),
                "away_id": fixture.get("VisitingTeamId", ""),
                "date": fixture.get("GameDateText", ""),
                "time": minutes_to_hhmm(fixture.get("GameTime", "")),
                "venue": fixture.get("SportFacilityDescription", ""),
            })

    # Results
    with open(results_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["league_id","date","time","home_id","home_score","away_id","away_score"], quoting=csv.QUOTE_ALL)
        for fixture in fixtures:
            if fixture.get("IsSubmittedForStandings") is False:
                continue 
            writer.writerow({
                "league_id": fixture.get("LeagueId", ""),
                "date": fixture.get("GameDateText", ""),
                "time": minutes_to_hhmm(fixture.get("GameTime", "")),
                "home_id": fixture.get("HomeTeamId", ""),
                "home_score": fixture.get("HomeTeamScore", ""),
                "away_id": fixture.get("VisitingTeamId", ""),
                "away_score": fixture.get("VisitingTeamScore", ""),
            })

    # Standings
    standings = data.get("Standings", [])
    with open(standings_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["league_id","team_id","pos","pld","w","d","l","pf","pa","diff","tf","ta","td","pts"], quoting=csv.QUOTE_ALL)
        for team in standings:
            writer.writerow({
                "league_id": team.get("LeagueId", ""),
                "team_id": team.get("TeamId", ""),
                "pos": team.get("Position", ""),
                "pld": team.get("GamesPlayed", ""),
                "w": team.get("Wins", ""),
                "d": team.get("Draws", ""),
                "l": team.get("Losses", ""),
                "pf": team.get("PointsFor", ""),
                "pa": team.get("PointsAgaints", ""),
                "diff": team.get("PointsDiff", ""),
                "tf": team.get("TriesFor", ""),
                "ta": team.get("TriesAgainst", ""),
                "td": team.get("TriesDiff", ""),
                "pts": team.get("PointsTotal", ""),
            })

print("All leagues saved to single CSVs")
