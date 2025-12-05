# csv_dictreader.py
import csv

FILENAME = "data.csv"
DATADIR = ""

with open(DATADIR + FILENAME, "rt", newline="") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0.0
    count = 0
    for row in reader:
        # row é um dicionário, ex: {'id': 1.0, 'age': 20.0, 'name': 'Joe'}
        total += row["age"]
        count += 1

    print(f"average is {total / count}")
