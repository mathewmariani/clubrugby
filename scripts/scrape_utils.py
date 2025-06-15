import requests
from bs4 import BeautifulSoup
import csv
import os

from datetime import datetime
import re

def parse_date(raw_date: str) -> str:
    """Convert various date formats to YYYY-MM-DD."""
    if raw_date.upper() in {"TBC", "TBA", ""}:
        return "TBC"
    raw_date = raw_date.strip()
    formats = [
        "%d/%m/%Y",     # 24/05/2025
        "%d-%m-%Y",     # 24-05-2025
        "%d %b %Y",     # 05 Jun 2025
        "%d %B %Y",     # 05 June 2025
        "%Y-%m-%d",     # Already correct
    ]
    for fmt in formats:
        try:
            parsed = datetime.strptime(raw_date, fmt)
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError(f"Unknown date format: {raw_date}")


def parse_time(raw_time: str) -> str:
    """Convert various time formats to HH:MM 24-hour format."""
    raw_time = raw_time.strip().lower()
    raw_time = re.sub(r"\s+", "", raw_time)  # e.g., '10:00 AM' → '10:00am'
    formats = [
        "%H:%M",       # 15:00
        "%I:%M%p",     # 10:00am or 10:00AM
        "%I%p",        # 3PM
    ]
    for fmt in formats:
        try:
            parsed = datetime.strptime(raw_time, fmt)
            return parsed.strftime("%H:%M")
        except ValueError:
            continue
    raise ValueError(f"Unknown time format: {raw_time}")

def get_soup(url):
    print(f"📥 Fetching: {url}")
    response = requests.get(url)
    if response.status_code == 404:
        raise ValueError(f"🚫 404 Not Found: {url}")
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")

def save_to_csv(filename, fieldnames, data, quoting=csv.QUOTE_ALL):
    print(f"📄 Saving data to {filename}...")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w+", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quotechar='"', quoting=quoting)
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ Saved {len(data)} records to {filename}")

def save_rows_to_csv(filename, header, rows):
    print(f"📄 Writing {len(rows)} rows to {filename}...")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w+", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"✅ Finished writing to {filename}")