# Delhi Law Firms Scraper

A Python-based web scraper that extracts publicly available information about Indian law firms from an online legal directory.

## Features

- Scrapes law firm names
- Extracts email addresses
- Extracts phone numbers
- Extracts city and state
- Extracts practice areas
- Supports automatic pagination
- Exports data to CSV
- Exports data to Excel

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- OpenPyXL

## Project Structure

```
delhi-law-firms-scraper/
│
├── crawler.py
├── parser.py
├── extractor.py
├── exporter.py
├── run.py
├── sources.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Sample Output

The scraper exports:

- law_firms.csv
- law_firms.xlsx

Extracted fields:

- Name
- Email
- Phone
- City
- State
- Practice Areas
- Description
- Profile URL

## Installation

```bash
git clone https://github.com/advocateprashantgautam-code/law-firms-scraper.git
cd law-firms-scraper
pip install -r requirements.txt
python run.py
```

## Future Improvements

- Extract complete address
- Extract official website
- Extract social media links
- Better Excel formatting
- Concurrent scraping for faster execution

## Author

**Advocate Prashant Gautam**