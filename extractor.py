import json
from bs4 import BeautifulSoup


class Extractor:

    def __init__(self, html):
        self.soup = BeautifulSoup(html, "lxml")

    def details(self):

        data = {
            "name": "",
            "email": "",
            "phone": "",
            "city": "",
            "state": "",
            "description": "",
            "practice_areas": ""
        }

        script = self.soup.find(
            "script",
            attrs={"type": "application/ld+json"}
        )

        if not script:
            return data

        try:
            obj = json.loads(script.string)

            data["name"] = obj.get("name", "")
            data["email"] = obj.get("email", "")
            data["phone"] = obj.get("telephone", "")
            data["description"] = obj.get("description", "")

            address = obj.get("address", {})
            data["city"] = address.get("addressLocality", "")
            data["state"] = address.get("addressRegion", "")

            knows = obj.get("knowsAbout", [])

            if isinstance(knows, list):
                data["practice_areas"] = ", ".join(knows)
            else:
                data["practice_areas"] = ""

            return data

        except Exception as e:
            print("Extractor Error:", e)
            return data