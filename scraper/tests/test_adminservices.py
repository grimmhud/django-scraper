from django.test import TestCase
from zipfile  import is_zipfile
from io import BytesIO
from ..services.AdminServices import ExportCsvMixin
from ..models import ScrapingResult


class ExportCsvMixinTestCase(TestCase):
    def setUp(self):
        self.sut = ExportCsvMixin()

    def test_return_is_status_code_200(self):
        queryset  = []
        queryset.append(ScrapingResult.objects.create(id=1,values=['row0']))
        queryset.append(ScrapingResult.objects.create(id=2,values=['row1']))

        response = self.sut.export_as_csv(None, queryset)

        self.assertEqual(200, response.status_code)

    def test_return_a_file_content(self):
        queryset  = []
        queryset.append(ScrapingResult.objects.create(id=1,values=['row0']))
        queryset.append(ScrapingResult.objects.create(id=2,values=['row1']))

        response = self.sut.export_as_csv(None, queryset)

        self.assertTrue(response['Content-Disposition'].endswith('web-scraping.zip'))
    
    def test_return_a_zipfile(self):
        queryset  = []
        queryset.append(ScrapingResult.objects.create(id=1,values=['row0']))
        queryset.append(ScrapingResult.objects.create(id=2,values=['row1']))

        response = self.sut.export_as_csv(None, queryset)
        
        self.assertTrue(is_zipfile(BytesIO(response.content)))