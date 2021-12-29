from django.shortcuts import  render
from django.http import HttpResponseNotFound, FileResponse
from django.views.generic import TemplateView
import json
import ast
from .services.FileConverter import to_csv
from .services.WebScraper import scrap_website

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name, {})
        
    def post(self, request):
        context = {}
        extracted_data = scrap_website(request.POST['website'], request.POST['path'])
        context['extracted_data'] = extracted_data

        return render(request, self.template_name, context)


def export_data(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        export_type = body['export_type']
        extracted_data = ast.literal_eval(body['extracted_data'])

        if export_type == '1':
            try:
                file_path = to_csv(extracted_data)
                response = FileResponse(open(file_path, 'rb'))
            except IOError:
                    response = HttpResponseNotFound()       
            return response