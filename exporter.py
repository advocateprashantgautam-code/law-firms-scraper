import csv
from openpyxl import Workbook


class Exporter:

    def __init__(self, data):
        self.data = data

    def csv(self, filename="law_firms.csv"):

        if not self.data:
            return

        fields = list(self.data[0].keys())

        with open(filename, "w", newline="", encoding="utf-8-sig") as f:

            writer = csv.DictWriter(f, fieldnames=fields)

            writer.writeheader()

            writer.writerows(self.data)

        print(f"\nCSV exported -> {filename}")

    def excel(self, filename="law_firms.xlsx"):

        if not self.data:
            return

        wb = Workbook()

        ws = wb.active

        ws.title = "Law Firms"

        headers = list(self.data[0].keys())

        ws.append(headers)

        for row in self.data:
            ws.append([row[h] for h in headers])

        wb.save(filename)

        print(f"Excel exported -> {filename}")