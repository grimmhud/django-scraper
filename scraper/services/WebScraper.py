from bs4 import BeautifulSoup
import requests
import time
import datetime


def scrap_website(url, path):
    soup = __get_html_content_as_soup(url)
    __extract_data(soup, path)

def __get_html_content_as_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml')
    
    
def __extract_data(soup, path):
    selected_content = soup.select(path)

    data = []
    for content in selected_content:
        data.append(content.text.strip())

    return data