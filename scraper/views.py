from django.shortcuts import redirect, render
from django.template import Context
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse


import json
from .services.FileConverter import to_csv
from .services.WebScraper import scrap_website


def home_view(request):
    context = {}
    if request.method == 'GET':
        context['user'] = request.META['USER']
        return render(request, 'home.html', context)
    if request.method == 'POST':
        print('home POST')
        extracted_data = scrap_website(request.POST['website'], request.POST['path'])
        #to_csv(extracted_data)
        print('home done')
        context['extracted_data'] = extracted_data
        return render(request, 'home.html', context)
    return render(request, 'home.html', {})