import csv
from datetime import datetime

def to_csv(data):
    now = datetime.now()
    with open(f'./../../scraper-history/scrapping-{now}.csv', 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow([row])
