import json
import re

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
        club_id = (club.get("clubId") or "").strip()
        name = (club.get("clubName") or "").strip()
        email = (club.get("email") or "").strip()
        province = (club.get("countryProvince") or "").strip()
        website = (club.get("webAddress") or "").strip()

        clubs.append({
            "id": club_id,
            "name": name,
            "email": email,
            "province": province,
            "website": website,
        })

        print(f"✅ Scraped club: {name} ({club_id})")


    return clubs
