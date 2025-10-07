import requests
url = "https://www.gov.uk/bank-holidays.json"
resp = requests.get(url, timeout=20); resp.raise_for_status()
data = resp.json()
first = data["northern-ireland"]["events"][0]
print(f"{first['title']} — {first['date']}")
print(first)
