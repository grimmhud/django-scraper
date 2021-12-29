from bs4 import BeautifulSoup
import requests
import ast


def scrap_website(url, path):
    soup = __get_html_content_as_soup(url)
    return __extract_data(soup, path)

def __get_html_content_as_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml')
    
    
def __extract_data(soup, path):
    selected_content = soup.select(path)

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