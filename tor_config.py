import requests
from stem.control import Controller

def start_tor_session():
    """Starts a Tor session using the SOCKS5 proxy."""
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session

def restart_tor():
    """Restarts Tor to get a new IP address."""
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_password')
        controller.signal(2)  # NEWNYM signal to get a new identity
        print("[+] Tor IP refreshed.")

if __name__ == "__main__":
    restart_tor()
