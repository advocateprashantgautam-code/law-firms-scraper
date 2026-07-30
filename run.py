from crawler import Crawler
from parser import Parser
from extractor import Extractor
from exporter import Exporter


def banner():

    print("=" * 70)
    print("Delhi Law Firms Scraper v1.0")
    print("=" * 70)


def collect_firms(crawler):

    next_page = "/browse-firms"

    visited = set()

    firms = []

    page = 1

    while next_page:

        print(f"\nScraping directory page {page}...")

        html = crawler.fetch(next_page)

        if not html:
            break

        parser = Parser(html)

        for firm in parser.firms():

            if firm["url"] not in visited:

                visited.add(firm["url"])

                firms.append(firm)

        next_page = parser.next_page()

        page += 1

    return firms


def scrape_details(crawler, firms):

    results = []

    total = len(firms)

    for index, firm in enumerate(firms, start=1):

        print(f"[{index}/{total}] {firm['name']}")

        html = crawler.fetch(firm["url"])

        if not html:
            continue

        extractor = Extractor(html)

        data = extractor.details()

        data["profile_url"] = crawler.base_url + firm["url"]

        results.append(data)

    return results


def main():

    banner()

    crawler = Crawler()

    firms = collect_firms(crawler)

    print(f"\nCollected {len(firms)} firms.")

    print("\nExtracting firm details...\n")

    data = scrape_details(crawler, firms)

    exporter = Exporter(data)

    exporter.csv()

    exporter.excel()

    print("\nDone!")

    print(f"Records exported: {len(data)}")


if __name__ == "__main__":
    main()