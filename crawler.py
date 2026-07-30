"""
crawler.py

Downloads HTML pages.
"""

import requests
from urllib.parse import urljoin


class Crawler:

    def __init__(self):

        self.base_url = "https://directory.legalfirms.in"

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/139.0 Safari/537.36"
            )
        }

        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def fetch(self, url):

        if not url.startswith("http"):
            url = urljoin(self.base_url, url)

        try:

            response = self.session.get(
                url,
                timeout=30,
            )

            response.raise_for_status()

            return response.text

        except Exception as e:

            print(f"[ERROR] {url}")
            print(e)

            return None

    def save_html(self, html, filename="output/page.html"):

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)