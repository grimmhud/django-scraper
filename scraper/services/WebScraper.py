from bs4 import BeautifulSoup
import requests
import time
import datetime


def extract_data():
    soup = get_html_content_as_soup()
    find_jobs(soup)

def get_html_content_as_soup():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
    return BeautifulSoup(html_text.text, 'lxml')

def save_job(file, company_name, skills, more_info):

    file.write(f'Company Name: {company_name}\n')
    file.write(f'Requirements Skills: {skills}\n')
    file.write(f'More info: {more_info}\n')
    file.write('\n')
    
def find_jobs(soup):
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    now = datetime.datetime.now()
    with open(f'/Users/hudson.oliveira/Documents/Projects/personal/scraper-history/jobs-{now}', 'w') as file:
        for job in jobs:
            skills = job.find('span', class_='srp-skills').text.strip().replace('  ,  ', ', ')
            
            posted_date = job.find('span', class_='sim-posted').text.strip()
            if 'few days' not in posted_date:
                continue

            company_name = job.find('h3', class_='joblist-comp-name').text.replace('(More Jobs)', '').strip()
            more_info = job.header.h2.a['href']
            save_job(file, company_name, skills, more_info)