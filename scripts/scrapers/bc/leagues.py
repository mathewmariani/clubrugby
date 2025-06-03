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

    for div in soup.find_all("div", class_="comp_list"):
        a_tag = div.find("a", href=True)
        name_tag = div.find("div", class_="compbox")

        if a_tag and name_tag:
            match = re.search(r'/league/(\d+)', a_tag["href"])
            if match:
                leagues.append({
                    "id": match.group(1),
                    "name": name_tag.get_text(strip=True),
                })

    return leagues
