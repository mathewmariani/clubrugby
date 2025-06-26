import re

def scrape(soup):
    """
    Scrapes league IDs and names from the competitions page.

    Args:
        soup (BeautifulSoup): Parsed HTML of the competitions page.

    Returns:
        List[List[str]]: A list of [id, name] rows for each league.
    """
    leagues = []

    for li in soup.find_all("li", class_="menu-item"):
        a_tag = li.find("a", href=True)
        

        if a_tag:
            match = re.search(r'/league/(\d+)', a_tag["href"])
            if match:
                leagues.append({
                    "id": match.group(1),
                    "name": a_tag.get_text(strip=True),
                })

    return leagues
