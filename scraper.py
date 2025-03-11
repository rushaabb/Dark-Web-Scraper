import requests
from bs4 import BeautifulSoup
from tor_config import start_tor_session

def scrape_onion_site(url):
    """Scrape a given .onion site through Tor."""
    session = start_tor_session()
    response = session.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.prettify()
    else:
        return f"Failed to access {url}: {response.status_code}"

if __name__ == "__main__":
    onion_url = "http://exampleonionurl.onion"
    print(scrape_onion_site(onion_url))
