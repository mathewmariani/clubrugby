import csv
from collections import defaultdict
from datetime import datetime, timedelta
import os

DATA_FOLDER = "public/data/qc/2025"  # Change this to your folder

def load_csv(filename):
    with open(os.path.join(DATA_FOLDER, filename), encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            # Strip whitespace from keys and values for safety
            row = {k.strip(): v.strip() for k, v in row.items()}
            rows.append(row)
        return rows

clubs = load_csv("clubs.csv")
results = load_csv("results.csv")
schedule = load_csv("schedule.csv")
standings = load_csv("standings.csv")
leagues = load_csv("leagues.csv")

club_lookup = {c["id"]: c["name"] for c in clubs}
league_lookup = {l["id"]: l["name"] for l in leagues}

def format_leagues():
    return "\n".join(f"- {l['id']}: {l['name']}" for l in leagues)

def format_clubs():
    return "\n".join(f"- {c['id']}: {c['name']}" for c in clubs)

def format_standings():
    league_groups = defaultdict(list)

    for row in standings:
        league_groups[row["league_id"]].append(row)

    output = []

    for league_id, teams in league_groups.items():
        # Sort teams by pts descending (float), then by diff descending, then by team name
        def sort_key(team):
            try:
                pts = float(team.get("pts", 0))
            except ValueError:
                pts = 0
            try:
                diff = float(team.get("diff", 0))
            except ValueError:
                diff = 0
            name = club_lookup.get(team["team_id"], "")
            return (-pts, -diff, name)

        sorted_teams = sorted(teams, key=sort_key)

        # Assign positions with ties: same pts and diff share same pos
        positions = []
        last_pts = None
        last_diff = None
        last_pos = 0
        skip = 0

        for i, team in enumerate(sorted_teams, start=1):
            try:
                pts = float(team.get("pts", 0))
            except ValueError:
                pts = 0
            try:
                diff = float(team.get("diff", 0))
            except ValueError:
                diff = 0
            if pts == last_pts and diff == last_diff:
                pos = last_pos
                skip += 1
            else:
                pos = last_pos + 1 + skip
                skip = 0
            last_pts = pts
            last_diff = diff
            last_pos = pos
            positions.append((pos, team))

        lines = []
        league_name = league_lookup.get(league_id, "Unknown League")
        lines.append(f"{league_name}:")
        for pos, team in positions:
            name = club_lookup.get(team["team_id"], "Unknown")
            w = team.get("w", "0")
            l = team.get("l", "0")
            d = team.get("d", "0")
            pts = team.get("pts", "0")
            lines.append(f"{pos}. {name}: {w}W-{d}D-{l}L, {pts} pts")
        output.append("\n".join(lines))

    return "\n\n".join(output)

def format_matches_to_cover():
    lines = []
    today = datetime.today()
    recent_cutoff = today - timedelta(days=5)
    future_cutoff = today + timedelta(days=7)

    # Past results (last 5 days) date format: YYYY-MM-DD
    for row in results:
        try:
            date_obj = datetime.strptime(row["date"], "%Y-%m-%d")
        except Exception:
            continue
        if recent_cutoff <= date_obj <= today:
            home = club_lookup.get(row["home_id"], "Unknown")
            away = club_lookup.get(row["away_id"], "Unknown")
            league_id = row["league_id"]
            league = league_lookup.get(league_id, "Unknown League")
            time = row.get("time", "Unknown time")
            venue = row.get("venue", "Unknown venue")
            # Compose line including all required fields for GPT prompt context
            line = f"- {league_id},{date_obj.strftime('%Y-%m-%d')},{time},{venue}: {home} {row['home_score']}–{row['away_score']} {away} ({league})"
            lines.append(line)

    # Upcoming matches (next 7 days) date format: DD/MM/YYYY
    for row in schedule:
        try:
            date_obj = datetime.strptime(row["date"], "%d/%m/%Y")
        except Exception:
            continue
        if today <= date_obj <= future_cutoff:
            home = club_lookup.get(row["home_id"], "Unknown")
            away = club_lookup.get(row["away_id"], "Unknown")
            league_id = row["league_id"]
            league = league_lookup.get(league_id, "Unknown League")
            time = row.get("time", "Unknown time")
            venue = row.get("venue", "Unknown venue")
            line = f"- {league_id},{date_obj.strftime('%Y-%m-%d')},{time},{venue}: {home} vs {away} ({league})"
            lines.append(line)

    return "\n".join(lines)

def generate_prompt():
    matches_text = format_matches_to_cover()
    prompt_text = f"""You're a professional rugby journalist. Based on the structured data below, generate exciting, short, and engaging headlines (max ~12 words) suitable for a rugby news website.

Use typical sports headline style — energetic, confident, sometimes dramatic. For matches that already happened, highlight surprising results, dominant wins, or rivalries. For upcoming games, tease drama, stakes, or potential clashes based on standings.

### Context:
Leagues:
{format_leagues()}

Clubs:
{format_clubs()}

Standings:
{format_standings()}

### Matches to Cover (format: league_id,date,time,venue: description):
{matches_text}

Write one headline per match.

Output the headlines as CSV rows with columns: league_id,date,time,venue,headline
Include this header line exactly as the first line:
league_id,date,time,venue,headline

No extra text or explanations, only the CSV rows.

Example:
league_id,date,time,venue,headline
premiership,2025-05-20,15:00,Stadium A,Tigers roar to thrilling victory
championship,2025-05-22,19:30,Field B,Falcons prepare to soar against Lions
"""
    return prompt_text

def main():
    prompt = generate_prompt()
    print(prompt)

if __name__ == "__main__":
    main()
