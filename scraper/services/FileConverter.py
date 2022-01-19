import csv
from io import StringIO
from zipfile import ZipFile

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
    with ZipFile(stream, 'w') as zf:
        for f in files:
            zf.writestr(f['filename'], f['file'].getvalue())
    return stream.getvalue()