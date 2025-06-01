import re
from scrape_utils import get_soup, save_rows_to_csv

URL = "https://rugbyquebec.org/schedule/"

def scrape_schedule_leagues(url=URL, save_path="data/leagues.csv", save=True):
    soup = get_soup(url)
    leagues = []
    print("🔍 Looking for league entries...")

    for div in soup.find_all("div", class_="comp_list"):
        a_tag = div.find("a", href=True)
        name_tag = div.find("div", class_="compbox")

        if a_tag and name_tag:
            match = re.search(r'/league/(\d+)', a_tag["href"])
            if match:
                comp_id = match.group(1)
                comp_name = name_tag.get_text(strip=True)
                leagues.append([comp_id, comp_name])
                print(f"✅ Found league: {comp_name} ({comp_id})")

    if save:
        save_rows_to_csv(f"{save_path}/schedule.csv", ["id", "name"], leagues)
        print("🎉 League scraping complete!")

    return leagues

if __name__ == "__main__":
    scrape_schedule_leagues()
