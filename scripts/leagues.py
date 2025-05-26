import re
from scrape_utils import get_soup, save_rows_to_csv

URL = "https://rugbyquebec.org/competitions/"
soup = get_soup(URL)

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

save_rows_to_csv("data/leagues.csv", ["id", "name"], leagues)
print("🎉 League scraping complete!")