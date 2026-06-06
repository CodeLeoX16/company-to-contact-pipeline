import requests
from config import PROSPEO_API_KEY


def search_people(company_domain):

    url = "https://api.prospeo.io/search-person"

    headers = {
        "X-KEY": PROSPEO_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "page": 1,
        "filters": {
            "company": {
                "websites": {
                    "include": [
                        company_domain
                    ]
                }
            }
        }
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            return []

        data = response.json()

        people = []

        for item in data.get("results", []):

            person = item.get("person", {})

            people.append({
                "person_id": person.get("person_id"),
                "name": person.get("full_name"),
                "title": person.get("current_job_title"),
                "linkedin": person.get("linkedin_url")
            })

        return people

    except Exception as e:

        print(
            f"Prospeo Error for {company_domain}: {e}"
        )

        return []