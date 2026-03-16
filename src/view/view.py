import configparser
import requests

import os
import subprocess

# Get the git repo root
REPO_ROOT = subprocess.check_output(
    ['git', 'rev-parse', '--show-toplevel'],
    text=True
).strip()

CONFIG_PATH = os.path.join(REPO_ROOT, 'final-project', 'config.ini')

# Load API key from cfg ini
config = configparser.ConfigParser()
config.read(CONFIG_PATH)
api_key = config.get('newsapi', 'api_key', fallback=None)

if not api_key:
    print(f"Could not load API key. Config path: {CONFIG_PATH}")
    print(f"File exists: {os.path.exists(CONFIG_PATH)}")
    print(f"Sections found: {config.sections()}")
    exit(1)
api_key = config['newsapi']['api_key']

def get_sources():
    """Fetch available news sources from NewsAPI."""
    url = f'https://newsapi.org/v2/sources?apiKey={api_key}'
    response = requests.get(url)
    data = response.json()

    if data.get('status') != 'ok':
        print(f"Error fetching sources: {data.get('message')}")
        return []

    return data.get('sources', [])

def display_sources(sources):
    """Display sources as a numbered list."""
    print("\n=== Available News Sources ===\n")
    for i, source in enumerate(sources, start=1):
        print(f"{i:>3}. {source['name']} ({source['category']}) - {source['country'].upper()}")
    print()

def get_headlines(source_id, source_name):
    """Fetch top headlines for the selected source."""
    url = (
        f'https://newsapi.org/v2/top-headlines?'
        f'sources={source_id}&'
        f'apiKey={api_key}'
    )
    response = requests.get(url)
    data = response.json()

    if data.get('status') != 'ok':
        print(f"Error fetching headlines: {data.get('message')}")
        return

    articles = data.get('articles', [])
    if not articles:
        print(f"No articles found for {source_name}.")
        return

    print(f"\n=== Top Headlines from {source_name} ===\n")
    for i, article in enumerate(articles, start=1):
        print(f"{i}. {article['title']}")
        if article.get('description'):
            print(f"   {article['description'][:120]}...")
        print(f"   URL: {article['url']}\n")

def main():
    print("Fetching news sources...")
    sources = get_sources()

    if not sources:
        print("No sources available. Check your API key or network connection.")
        return

    while True:
        display_sources(sources)

        user_input = input("Enter a number to view headlines (or 'q' to quit): ").strip()

        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        if not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        index = int(user_input) - 1

        if index < 0 or index >= len(sources):
            print(f"Please enter a number between 1 and {len(sources)}.")
            continue

        selected = sources[index]
        get_headlines(selected['id'], selected['name'])

        again = input("\nPress Enter to go back to the list, or 'q' to quit: ").strip()
        if again.lower() == 'q':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()
