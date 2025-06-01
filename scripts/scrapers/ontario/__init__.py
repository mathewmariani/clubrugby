
from .clubs import scrape as scrape_clubs
from .leagues import scrape as scrape_leagues
from .fixtures import scrape as scrape_fixtures
from .results import scrape as scrape_results
from .standings import scrape as scrape_standings
# from .info import scrape as scrape_info

__all__ = ["scrape_clubs", "scrape_leagues", "scrape_fixtures", "scrape_results", "scrape_standings"]#, "scrape_info"]