from django.shortcuts import  render
from django.http import HttpResponseNotFound, FileResponse, HttpResponse
from django.views.generic import TemplateView
import json
from .models import ScrapingResult
from .services.FileConverter import to_csv
from .services.WebScraper import scrap_website

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name, {})
        
    def post(self, request):
        context = {}
        scraping_result = scrap_website(request.POST['website'], request.POST['path'])
        context['scraping_result'] = scraping_result

        return render(request, self.template_name, context)


def export_data(request):
    if request.method == 'GET':     
        export_type = request.GET.get('export_type')
        scraping_result_id = request.GET.get('scraping_result_id')
        

        result_model = ScrapingResult.objects.get(id=scraping_result_id)

        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
        )
        if export_type == '1':
            try:
                to_csv(response, result_model.values)
            except IOError:
                    response = HttpResponseNotFound()       
            return response