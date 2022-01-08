from bs4 import BeautifulSoup
import requests
import ast
from ..models import ScrapingSearch, ScrapingResult


def scrap_website(url, filter):
    soup = __get_html_content_as_soup(url)
    data =  __extract_data(soup, filter)    
    return __save_and_get_scraping_result(url, filter, data)

def __get_html_content_as_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml')
    
    
def __extract_data(soup, filter):
    selected_content = soup.select(filter)

    data = []
    for content in selected_content:
        data.append(content.text.strip())

    return __clean_data(data)

def __clean_data(data):
    data_str = str(data)
    if '\\n' in data_str or '\\r' in data_str:
        data_str = data_str.replace('\\r','').replace('\\n','')
    if '\n' in data_str or '\r' in data_str:
        data_str =  data_str.replace('\r','').replace('\n','')

    return ast.literal_eval(data_str)


def __save_and_get_scraping_result(url, filter, data):
    result = ScrapingResult.create(data)
    result.save()
    search = ScrapingSearch.create(url, filter, result)
    search.save()
    return result