import requests

def process_webhook(url, data):
    # VULNERABLE: SSRF - user controls the URL
    response = requests.get(url)
    return response.json()

def fetch_user_avatar(avatar_url):
    # VULNERABLE: no URL validation
    return requests.get(avatar_url).content
