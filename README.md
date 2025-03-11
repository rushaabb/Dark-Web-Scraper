# Dark Web Scraper

Overview

A Python-based scraper that accesses .onion websites through the Tor network and extracts data.

Features

Uses Tor to browse hidden services.

Scrapes .onion sites securely.

Supports IP rotation using Tor’s control port.

Prerequisites

Python 3.x

Tor (Must be installed and running)

Install Tor

Linux (Debian/Ubuntu)

sudo apt update && sudo apt install tor -y

Windows

Download and install Tor Browser from torproject.org.

Installation

# Clone the repository
git clone https://github.com/YOUR-USERNAME/Dark-Web-Scraper.git
cd Dark-Web-Scraper

# Install dependencies
pip install -r requirements.txt

Usage

1. Start Tor Service

Run Tor in the background:

tor &

2. Run the Scraper

python3 src/scraper.py

Notes

Ensure Tor service is running before executing the script.

Modify scraper.py to scrape specific .onion sites.

License

This project is licensed under the MIT License.

