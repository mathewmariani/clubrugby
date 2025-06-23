import json
import re
from .exclusions import excluded_teams

def scrape(soup):
    clubs = []

    script_tag = None
    for script in soup.find_all("script"):
        if script.string and "var clubListData =" in script.string:
            script_tag = script.string
            break

    if not script_tag:
        print("❌ Could not find the 'clubListData' script tag")
        return []

    match = re.search(r"var clubListData\s*=\s*(\[\{.*?\}\]);", script_tag, re.DOTALL)
    if not match:
        print("❌ Could not extract JSON array from script")
        return []

    json_text = match.group(1)
    data = json.loads(json_text)

    for club in data:
        id = (club.get("clubId") or "").strip()
        name = (club.get("clubName") or "").strip()
        logo = (club.get("clubImage") or "").strip()

        if id in excluded_teams:
            continue

        clubs.append({
            "id": id,
            "name": name,
            "logo_url": logo,
        })

    return clubs
