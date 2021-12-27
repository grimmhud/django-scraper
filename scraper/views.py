from django.shortcuts import render
from .services.WebScraper import extract_data

def home_view(request):
    if request.method == 'GET':
        print('GET')
        return render(request, 'home.html', {})
    if request.method == 'POST':
        print('POST')
        print(request.body)
        extract_data()
        return render(request, 'home.html', {})
    
    print('None')
    return render(request, 'home.html', {})