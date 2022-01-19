from django.test import TestCase
from io import BytesIO, StringIO
from zipfile import ZipFile, is_zipfile
from ..services.FileConverter import create_csv_with_stream, create_csv, zipFiles


class FileConverterTestCase(TestCase):
    def test_return_all_values_in_stream(self):
        stream = StringIO()
        rows = ['row-1', 'row-2', 'row-3']
        create_csv_with_stream(stream, rows)
        csv_data = stream.getvalue()
        for row in rows:
            self.assertIn(row, csv_data)
    
    def test_return_all_values_and_stream(self):
        rows = ['row-1', 'row-2', 'row-3']
        stream = create_csv(rows)
        csv_data = stream.getvalue()
        for row in rows:
            self.assertIn(row, csv_data)

    def test_return_a_zip_file(self):
        files = []
        files.append({'filename': 'name', 'file': create_csv(['row-1'])})
        
        zip = BytesIO()
        zipFiles(zip, files)

        self.assertTrue(is_zipfile(zip))

    def test_return_a_correct_file_compressed(self):
        files = []
        rows = ['row-1', 'row-2', 'row-3']
        files.append({'filename': 'name.csv', 'file': create_csv(rows)})
        
        zip = BytesIO()
        zipFiles(zip, files)

        x = ZipFile(zip)
        self.assertEqual(files[0]['filename'], x.namelist()[0])

    def test_return_a_correct_file_compressed_with_correct_data(self):
        files = []
        rows = ['row-1', 'row-2', 'row-3']
        files.append({'filename': 'name.csv', 'file': create_csv(rows)})
        
        zip = BytesIO()
        zipFiles(zip, files)

        zipfile = ZipFile(zip)
        csv = zipfile.open(files[0]['filename'])
        csv_data = csv.read().decode("utf-8")
        for row in rows:
            self.assertIn(row, csv_data)

    