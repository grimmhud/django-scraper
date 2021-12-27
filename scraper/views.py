from django.shortcuts import render
import json
from .services.FileConverter import to_csv
from .services.WebScraper import scrap_website


def home_view(request):
    if request.method == 'GET':
        print('GET')
        return render(request, 'home.html', {})
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        data = scrap_website(body['website'], body['path'])
        to_csv(data)
        return render(request, 'home.html', {})
    
    print('None')
    return render(request, 'home.html', {})