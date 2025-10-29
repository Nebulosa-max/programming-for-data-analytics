# assignment02-bankholidays.py
import requests

URL = "https://www.gov.uk/bank-holidays.json"

def fetch_holidays():
    r = requests.get(URL, timeout=20)
    r.raise_for_status()
    return r.json()

def dates_for(region, data):
    """Return a set of YYYY-MM-DD strings for a region key in the JSON."""
    return {ev["date"] for ev in data[region]["events"]}

def main():
    data = fetch_holidays()

    # Regions in the dataset
    NI = "northern-ireland"
    EW = "england-and-wales"
    SC = "scotland"

    ni_dates = dates_for(NI, data)
    ew_dates = dates_for(EW, data)
    sc_dates = dates_for(SC, data)

    # ----- Part 1: all NI bank-holiday dates -----
    print("All Northern Ireland bank-holiday dates:")
    for d in sorted(ni_dates):
        print(d)

    print("\nUnique to Northern Ireland (not in England & Wales or Scotland):")
    unique_to_ni = ni_dates - (ew_dates | sc_dates)
    if not unique_to_ni:
        print("(none)")
    else:
        ni_date_to_title = {ev["date"]: ev["title"] for ev in data[NI]["events"]}
        for d in sorted(unique_to_ni):
            print(f"{d} — {ni_date_to_title.get(d, '')}")

if __name__ == "__main__":
    main()
