from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseServerError
from .WebScraper import scrap_website
from ..models import ScrapingSearch, ScrapingResult
from .FileConverter import create_csv_with_stream

class HomeViewService:
    @classmethod
    def post(cls, request, template_name):
        try:
            context = {}
            website = request.POST['website']
            filter = request.POST['filter']
            
            data = scrap_website(website, filter)
            scraping_result = cls.__save_and_get_scraping_result(website, filter, data)
            
            context['scraping_result'] = scraping_result
            return render(request, template_name, context)
        except Exception as e:
            msg = str(e)
            print(msg)
            return HttpResponseServerError(msg)
    
    def __save_and_get_scraping_result(url, filter, data):
        result = ScrapingResult.create(data)
        result.save()
        search = ScrapingSearch.create(url, filter, result)
        search.save()
        return result

class ExportDataViewService:
    csv_type = '1'
    @classmethod
    def get(cls, request):
        try:
            export_type = request.GET.get('export_type')
            scraping_result_id = request.GET.get('scraping_result_id')
            
            result_model = ScrapingResult.objects.get(id=scraping_result_id)

            response = HttpResponse(
                content_type='text/csv',
                headers={'Content-Disposition': 'attachment;'},
            )
            if export_type == cls.csv_type:
                create_csv_with_stream(response, result_model.values)
                return response
            return HttpResponseNotFound()
        except Exception as e:
            msg = str(e)
            print(msg)
            return HttpResponseServerError(msg)