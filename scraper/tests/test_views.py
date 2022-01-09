from django.test import TestCase
from django.utils import timezone
from scraper.models import ScrapingResult
from ..views import HomeView, export_data
from django.test.client import RequestFactory


class HomeViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.home_view = HomeView()

    def test_get_return_200ok(self):
        request = self.factory.get('/')
        response = self.home_view.get(request)

        self.assertTrue(response.status_code == 200)

    def test_post_template_name(self):
        request = self.factory.post('/')
        request.POST._mutable = True
        request.POST.appendlist('website','https://google.com')
        request.POST.appendlist('path','html > body')

        response = self.home_view.post(request)

        self.assertTrue(response.status_code == 200)


class ExportDataTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.scraping_result = ScrapingResult.objects.create(id=1, values=['row-1'], created_at=timezone.now())

    def test_get_return_200ok(self):
        request = self.factory.get('/export')
        
        request.GET._mutable = True
        request.GET.appendlist('export_type','1')
        request.GET.appendlist('scraping_result_id','1')
        
        response = export_data(request)

        self.assertTrue(response.status_code == 200)

    def test_get_return_content_correctly(self):
        request = self.factory.get('/export')
        
        request.GET._mutable = True
        request.GET.appendlist('export_type','1')
        request.GET.appendlist('scraping_result_id','1')
        
        response = export_data(request)
        content = response.content.decode("utf-8").strip()
        self.assertIn(content, self.scraping_result.values)

    def test_get_return_400notFound_when_export_type_doesnt_exists(self):
        request = self.factory.get('/export')
        
        request.GET._mutable = True
        request.GET.appendlist('export_type','2')
        request.GET.appendlist('scraping_result_id','1')
        
        response = export_data(request)

        self.assertTrue(response.status_code == 404)