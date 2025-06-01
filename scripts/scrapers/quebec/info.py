def scrape(soups_by_club):
    club_info = []

    for club_id, (club_name, soup) in soups_by_club.items():
        reg_url = email = ""
        try:
            right_fir = soup.find("div", class_="right_fir")

            if right_fir:
                links = right_fir.find_all("a", href=True)
                if len(links) > 0:
                    reg_url = links[0]["href"].strip()
                if len(links) > 1 and links[1]["href"].startswith("mailto:"):
                    email = links[1]["href"].replace("mailto:", "").strip()

            club_info.append({
                "id": club_id,
                "name": club_name,
                "url": reg_url,
                "email": email,
            })
            print(f"✅ Scraped info for {club_name} ({club_id})")
        except Exception as e:
            print(f"❌ Failed to parse {club_name} ({club_id}): {e}")
            club_info.append({
                "id": club_id,
                "name": club_name,
                "url": "",
                "email": "",
            })

    return club_info
