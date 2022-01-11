from django.test import TestCase
from ..services.FileConverter import to_csv
from io import StringIO

class FileConverterTestCase(TestCase):
    def test_return_all_values_in_stream(self):
        stream = StringIO()
        rows = ['row-1', 'row-2', 'row-3']
        to_csv(stream, rows)
        for row in rows:
            self.assertIn(row, stream.getvalue())