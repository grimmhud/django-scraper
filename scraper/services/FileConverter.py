import csv
from io import StringIO
import zipfile

def create_csv_with_stream(stream, data):  
    writer = csv.writer(stream)
    for row in data:
        writer.writerow([row])


def create_csv(data):  
    stream = StringIO()
    writer = csv.writer(stream)
    for row in data:
        writer.writerow([row])
    return stream


def zipFiles(stream, files):
    with zipfile.ZipFile(stream, 'w') as zf:
        for f in files:
            zf.writestr("{}.csv".format(f['filename']), f['file'].getvalue())
    return stream.getvalue()