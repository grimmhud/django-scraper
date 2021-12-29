import csv
import os
from datetime import datetime

def to_csv(data):
    now = datetime.now()
    base_path = './scraper-history/'
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    full_path = f'{base_path}scrapping-{now}.csv'
    with open(full_path, 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow([row])
    return full_path