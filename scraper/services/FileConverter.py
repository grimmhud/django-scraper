import csv
from datetime import datetime
import io
import base64

def to_csv(stream, data):  
    writer = csv.writer(stream)
    for row in data:
        writer.writerow([row])