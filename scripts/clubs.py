import re
from scrape_utils import get_soup, save_to_csv

URL = "https://rugbyquebec.org/clubs/"

def scrape_clubs(url=URL, save_path="data/", save=True):
    soup = get_soup(url)
    clubs = []
    print("🔍 Scanning club entries...")

    for li in soup.find_all("li"):
        club_div = li.find("div", class_="clubmap1")
        if not club_div:
            continue

        logo_url = club_div.find("img")["src"].strip() if club_div.find("img") else ""
        a_tag = club_div.find("a", href=True)
        if not a_tag:
            continue

        match = re.search(r'/clubprofile/(\d+)/', a_tag["href"])
        club_name = a_tag.find("h2").get_text(strip=True) if a_tag.find("h2") else ""

        if match:
            clubs.append({
                "id": match.group(1),
                "name": club_name,
                "logo_url": logo_url
            })
            print(f"✅ Found: {club_name} ({match.group(1)})")

    if save:
        save_to_csv(f"{save_path}/clubs.csv", ["id", "name", "logo_url"], clubs)
        print("🎉 Club scraping complete!")

    return clubs

if __name__ == "__main__":
    scrape_clubs()
