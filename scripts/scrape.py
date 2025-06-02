import importlib
import os
from datetime import datetime
from scrape_utils import get_soup, save_to_csv
from league_utils import load_team_id_map, load_league_ids, load_clubs

SCRAPERS = {
    "qc": {
        # "clubs": {
        #     "url": "https://rugbyquebec.org/clubs/",
        #     "module": "scrapers.qc.clubs",
        # },
        # "leagues": {
        #     "url": "https://rugbyquebec.org/competitions/",
        #     "module": "scrapers.qc.leagues",
        # },
        # "fixtures": {
        #     "url": "https://rugbyquebec.org/league/{}/",
        #     "module": "scrapers.qc.fixtures",
        # },
        # "results": {
        #     "url": "https://rugbyquebec.org/league/{}/",
        #     "module": "scrapers.qc.results",
        # },
        # "standings": {
        #     "url": "https://rugbyquebec.org/league/{}/",
        #     "module": "scrapers.qc.standings",
        # },
    },
    "on": {
        # "clubs": {
        #     "url": "https://www.rugbyontario.com/club-info/",
        #     "module": "scrapers.on.clubs",
        # },
        # "leagues": {
        #     "url": "https://www.rugbyontario.com/competitions/",
        #     "module": "scrapers.on.leagues",
        # },
        # "fixtures": {
        #     "url": "https://rugbyontario.com/league/{}/",
        #     "module": "scrapers.on.fixtures",
        # },
        # "results": {
        #     "url": "https://rugbyontario.com/league/{}/",
        #     "module": "scrapers.on.results",
        # },
        # "standings": {
        #    "url": "https://rugbyontario.com/league/{}/",
        #     "module": "scrapers.on.standings",
        # },
    },
    "ns": {
        # "clubs": {
        #     "url": "https://rugbyns.ns.ca/club-listing/",
        #     "module": "scrapers.ns.clubs",
        # },
        # "leagues": {
        #     "url": "https://rugbyns.ns.ca/competitions/",
        #     "module": "scrapers.ns.leagues",
        # },
        # "fixtures": {
        #     "url": "https://rugbyns.ns.ca/league/{}/",
        #     "module": "scrapers.ns.fixtures",
        # },
        # "results": {
        #     "url": "https://rugbyns.ns.ca/league/{}/",
        #     "module": "scrapers.ns.results",
        # },
        # "standings": {
        #    "url": "https://rugbyns.ns.ca/league/{}/",
        #     "module": "scrapers.ns.standings",
        # },
    },
}

def scrape(federation, datatype, save_path="data", save=True):
    config = SCRAPERS[federation][datatype]
    scraper = importlib.import_module(config["module"])

    if not hasattr(scraper, "scrape"):
        print(f"❌ {config['module']} missing scrape() function")
        return

    current_year = datetime.now().year
    federation_path = os.path.join(save_path, federation, str(current_year))
    os.makedirs(federation_path, exist_ok=True)

    if datatype in ("fixtures", "results", "standings"):
        url_template = config["url"]
        league_ids = load_league_ids(federation_path)
        team_id_map = load_team_id_map(federation_path)

        soups_by_league = {}
        for league_id in league_ids:
            url = url_template.format(league_id)
            try:
                print(f"📥 Fetching: {url}")
                soup = get_soup(url)
                soups_by_league[league_id] = soup
            except Exception as e:
                print(f"❌ Failed to fetch {url}: {e}")

        items = scraper.scrape(soups_by_league, team_id_map)
    elif datatype == "info":
        # Club info pages are individual per club
        url_template = config["url"]
        clubs = load_clubs(federation_path)

        soups_by_club = {}
        for club in clubs:
            club_id = club["id"]
            club_name = club["name"]
            url = url_template.format(club_id)

            try:
                print(f"📥 Fetching: {url}")
                soup = get_soup(url)
                soups_by_club[club_id] = (club_name, soup)
            except Exception as e:
                print(f"❌ Failed to fetch {url}: {e}")
                soups_by_club[club_id] = (club_name, None)

        items = scraper.scrape(soups_by_club)
    else:
        url = config["url"]
        print(f"📥 Fetching: {url}")
        soup = get_soup(url)
        items = scraper.scrape(soup)

    if not items:
        print(f"⚠️ No {datatype} found for {federation}")
        return

    if save:
        csv_file = os.path.join(federation_path, f"{datatype}.csv")
        keys = items[0].keys() if isinstance(items[0], dict) else None
        save_to_csv(csv_file, keys, items)
        print(f"✅ Saved to {csv_file}")

if __name__ == "__main__":
    for federation, datatypes in SCRAPERS.items():
        for datatype in datatypes:
            print(f"\n🔄 Starting scrape for {federation} - {datatype}")
            scrape(federation, datatype)
