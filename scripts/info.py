from scrape_utils import get_soup, save_rows_to_csv
import csv

print("📖 Loading club list from clubs.csv...")
with open("data/clubs.csv", newline='', encoding='utf-8') as f:
    clubs = list(csv.DictReader(f))

club_info = []

for club in clubs:
    url = f"https://rugbyquebec.org/clubprofile/{club['id']}/"
    try:
        soup = get_soup(url)
        right_fir = soup.find("div", class_="right_fir")
        reg_url = email = ""

        if right_fir:
            links = right_fir.find_all("a", href=True)
            if len(links) > 0:
                reg_url = links[0]["href"].strip()
            if len(links) > 1 and links[1]["href"].startswith("mailto:"):
                email = links[1]["href"].replace("mailto:", "").strip()

        club_info.append([club["id"], club["name"], reg_url, email])
        print(f"✅ Scraped info for {club['name']} ({club['id']})")

    except Exception as e:
        print(f"❌ Failed to scrape {club['name']} ({club['id']}): {e}")
        club_info.append([club["id"], club["name"], "", ""])

save_rows_to_csv("data/info.csv", ["id", "name", "url", "email"], club_info)
print("🎉 Club info scraping complete!")