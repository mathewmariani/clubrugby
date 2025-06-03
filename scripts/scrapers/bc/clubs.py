import re

def scrape(soup):
    """
    Scrapes club information from Rugby Quebec's clubs page.
    
    Args:
        soup (BeautifulSoup): Parsed HTML from the clubs page.
    
    Returns:
        List[Dict]: List of clubs with 'id', 'name', and 'logo_url'.
    """
    clubs = []

    for li in soup.find_all("li"):
        club_div = li.find("div", class_="clubmap1")
        if not club_div:
            continue

        logo_url = club_div.find("img")["src"].strip() if club_div.find("img") else ""
        a_tag = club_div.find("a", href=True)
        if not a_tag:
            continue

        match = re.search(r'/clubprofile/(\d+)', a_tag["href"])
        name = a_tag.find("h2").get_text(strip=True) if a_tag.find("h2") else ""

        if match:
            clubs.append({
                "id": match.group(1),
                "name": name,
                "logo_url": logo_url
            })

    return clubs
