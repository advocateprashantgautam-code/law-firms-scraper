# Delhi Law Firms Scraper

A Python-based web scraper that extracts publicly available information about Indian law firms from a legal directory and exports the data into CSV and Excel formats.

---

## Features

- Scrapes law firm names
- Extracts email addresses
- Extracts phone numbers
- Extracts city and state
- Extracts practice areas
- Extracts profile descriptions
- Supports automatic pagination
- Exports data to CSV
- Exports data to Excel
- Modular Python architecture

---

## Tech Stack

- Python 3
- Requests
- BeautifulSoup4
- OpenPyXL

---

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
├── .gitignore
├── law_firms.csv
└── law_firms.xlsx
```

---

## Output

The scraper generates two output files:

- `law_firms.csv`
- `law_firms.xlsx`

Each record contains:

- Law Firm Name
- Email Address
- Phone Number
- City
- State
- Practice Areas
- Description
- Profile URL

---

## Installation

Clone the repository:

```bash
git clone https://github.com/advocateprashantgautam-code/law-firms-scraper.git
```

Move into the project directory:

```bash
cd law-firms-scraper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the scraper:

```bash
python run.py
```

---

## Future Improvements

- Extract complete office address
- Extract official website
- Extract social media links
- Improve Excel formatting
- Add concurrent scraping
- Add logging and retry mechanism

---

## Author

**Advocate Prashant Gautam**

Advocate | Litigation | Python | Legal Automation

---

## Disclaimer

This project extracts only publicly available information for educational and research purposes. Users are responsible for complying with applicable laws, website terms of use, and privacy requirements.