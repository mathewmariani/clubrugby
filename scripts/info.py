from league_utils import load_clubs
from scrape_utils import get_soup, save_rows_to_csv

def scrape_info(clubs=None, save_path="data/", save=True):
    if clubs is None:
        clubs = load_clubs(save_path)

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

    if save:
        save_rows_to_csv(f"{save_path}/info.csv", ["id", "name", "url", "email"], club_info)
        print("🎉 Club info scraping complete!")

    return club_info

if __name__ == "__main__":
    scrape_info()
