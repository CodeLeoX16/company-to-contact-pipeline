import requests
from config import OCEAN_API_KEY

BASE_URL = "https://api.ocean.io"


def find_companies(seed_domain):

    url = f"{BASE_URL}/v3/search/companies"

    headers = {
        "X-Api-Token": OCEAN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "companiesFilters": {
            "lookalikeDomains": [
                seed_domain
            ]
        },
        "size": 10
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    data = response.json()

    companies = []

    for item in data.get("companies", []):

        company = item.get("company", {})

        companies.append({
            "name": company.get("name"),
            "domain": company.get("domain")
        })

    return companies