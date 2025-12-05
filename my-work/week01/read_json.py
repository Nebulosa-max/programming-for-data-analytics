import requests, json
url = "https://www.gov.uk/bank-holidays.json"
resp = requests.get(url, timeout=20); resp.raise_for_status()
data = resp.json()
print(json.dumps(data, indent=2)[:5000])
