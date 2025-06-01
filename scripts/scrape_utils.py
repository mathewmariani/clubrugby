import requests
from bs4 import BeautifulSoup
import csv
import os

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