from django.shortcuts import render
from django.views.generic import TemplateView
from .services.WebScraper import scrap_website
from .services.ViewServices import HomeViewService, ExportDataViewService

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name, {})
        
    def post(self, request):
        return HomeViewService.post(request, self.template_name)

def export_data(request):
    if request.method == 'GET':  
        return ExportDataViewService.get(request)   
