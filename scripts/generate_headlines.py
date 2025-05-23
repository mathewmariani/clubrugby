import os
import openai
from openai import OpenAI

# Create a client using your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

matches = [
    {"home": "Tigers", "away": "Falcons", "date": "2025-05-25"},
    {"home": "Lions", "away": "Bears", "date": "2025-05-26"},
]

def generate_headline(match):
    prompt = (
        f"Generate a short and catchy sports news headline for the following upcoming match:\n\n"
        f"{match['home']} vs {match['away']} on {match['date']}.\n\n"
        "Make it sound exciting and use typical sports headline language."
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50,
        temperature=0.8,
    )
    
    return response.choices[0].message.content.strip()

def main():
    for match in matches:
        headline = generate_headline(match)
        print(f"{match['home']} vs {match['away']} ({match['date']}): {headline}")

if __name__ == "__main__":
    main()
