import re
from .exclusions import excluded_leagues

def scrape(soup):
    """
    Scrapes league IDs and names from the competitions page.

    Args:
        soup (BeautifulSoup): Parsed HTML of the competitions page.

    Returns:
        List[dict]: A list of {"id": id, "name": name} dicts for each league.
    """
    leagues = []

    # Find all <a> tags where href contains /league/ and data-name attribute exists
    for a_tag in soup.find_all("a", href=True, attrs={"data-name": True}):
        match = re.search(r'/league/(\d+)', a_tag["href"])
        if match:
            id = match.group(1)

            if id in excluded_leagues:
                continue

            leagues.append({
                "id": id,
                "name": a_tag["data-name"].strip()
            })

    return leagues
