from ocean import find_companies
from prospeo import search_people

import pandas as pd
import time
from datetime import datetime


def main():

    print("=" * 50)
    print("OUTREACH PIPELINE")
    print("=" * 50)

    seed_domain = input(
        "\nEnter company domain (example: stripe.com): "
    ).strip()

    log_file = open(
        "../logs/run.log",
        "a",
        encoding="utf-8"
    )

    log_file.write(
        f"\n\nRun Started: {datetime.now()}\n"
    )

    print("\nSearching similar companies...\n")

    companies = find_companies(seed_domain)

    if not companies:
        print("No companies found.")
        return

    all_rows = []

    for company in companies:

        company_name = company.get("name")
        company_domain = company.get("domain")

        print(
            f"Processing {company_name} ({company_domain})"
        )

        log_file.write(
            f"Processing: {company_name} ({company_domain})\n"
        )

        try:

            people = search_people(company_domain)

            if not people:
                continue

            for person in people:

                all_rows.append({
                    "Company": company_name,
                    "Company_Domain": company_domain,
                    "Name": person.get("name"),
                    "Title": person.get("title"),
                    "LinkedIn": person.get("linkedin"),
                    "Person_ID": person.get("person_id")
                })

            time.sleep(2)

        except Exception as e:

            print(
                f"Error processing {company_domain}: {e}"
            )

            log_file.write(
                f"ERROR: {company_domain} -> {e}\n"
            )

    if len(all_rows) == 0:

        print("\nNo leads found.")

        log_file.write(
            "No leads generated.\n"
        )

        log_file.close()

        return

    df = pd.DataFrame(all_rows)

    df.drop_duplicates(
        subset=["LinkedIn"],
        inplace=True
    )

    df.to_csv(
        "../output/leads.csv",
        index=False
    )

    print(
        f"\nSaved {len(df)} leads to output/leads.csv"
    )

    log_file.write(
        f"Generated {len(df)} leads\n"
    )

    log_file.write(
        "Run Completed\n"
    )

    log_file.close()


if __name__ == "__main__":
    main()