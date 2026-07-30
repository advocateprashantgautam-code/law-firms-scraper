from bs4 import BeautifulSoup


class Parser:

    def __init__(self, html):
        self.soup = BeautifulSoup(html, "lxml")

    def title(self):
        if self.soup.title:
            return self.soup.title.text.strip()
        return "No Title"

    def firms(self):

        firms = []

        for card in self.soup.select("a.firm-card"):

            name = card.select_one(".firm-name")

            if not name:
                continue

            firms.append({
                "name": name.get_text(strip=True),
                "url": card.get("href")
            })

        return firms

    def next_page(self):

        next_link = self.soup.select_one('a[href*="page="][aria-label="Next"], a[href*="page="]:contains("Next")')

        if next_link:
            return next_link.get("href")

        # Fallback
        for link in self.soup.select('a[href*="page="]'):
            if link.get_text(strip=True).lower() == "next":
                return link.get("href")

        return None