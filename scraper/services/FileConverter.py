import csv

def to_csv(stream, data):  
    writer = csv.writer(stream)
    for row in data:
        writer.writerow([row])