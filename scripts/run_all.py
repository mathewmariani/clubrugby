import os
from clubs import scrape_clubs
from info import scrape_info
from leagues import scrape_leagues
from fixtures import scrape_fixtures
from results import scrape_results
from standings import scrape_standings
from datetime import datetime

def run_all():
    current_year = datetime.now().year
    path = f"data/{current_year}/qc"

    print("Starting full scrape sequence...\n")
    scrape_clubs(save_path=path)
    # scrape_info(save_path=path)
    # scrape_leagues(save_path=path)
    # scrape_fixtures(save_path=path)
    # scrape_results(save_path=path)
    # scrape_standings(save_path=path)
    print("\nAll scraping tasks complete!")

if __name__ == "__main__":
    run_all()
