from django.shortcuts import render
from .services.WebScraper import scrap_website
import json

def home_view(request):
    if request.method == 'GET':
        print('GET')
        return render(request, 'home.html', {})
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        scrap_website(body['website'], body['path'])
        return render(request, 'home.html', {})
    
    print('None')
    return render(request, 'home.html', {})