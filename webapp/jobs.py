from datetime import datetime
import requests


def count_words_at_url(url):
    if not url.startswith('http'):
        url = f'http://{url}'

    resp = requests.get(url)
    timestamp = datetime.now()
    print(f"\t\t[{timestamp}] Status_code for URL {url}: {resp.status_code}")
    return len(resp.text.split())
