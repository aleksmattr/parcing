import requests
from bs4 import BeautifulSoup
from pprint import pprint


HEADERS = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
    "accept": "text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8"
}

URL = "https://almaty.hh.kz/search/vacancy"
DOMEN = "https://almaty.hh.kz"


def get_html(url, headers=HEADERS, params=None):
    response = requests.get(url, headers=headers, params=params)
    print(response.url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    return response


def get_content(soup: BeautifulSoup):
    items = soup.find_all('div', class_='serp-item')
    data = []
    for item in items:
        name = item.find('a', class_='serp-item__title').get_text(strip=True)
        link = item.find('a', class_='serp-item__title').get('href')
        city = item.find_all('div', class_='bloko-text')[1].get_text(strip=True)
        comp = item.find('a', class_='bloko-link bloko-link_kind-tertiary').get_text(strip=True)
        try:
            zp = item.find('span', class_='bloko-header-section-3').get_text(strip=True)
        except:
            zp = 'no data available'
        try:
            online = item.find('div', class_='online-accounts--tWT3_ck7eF8Iv5SpZ6WL').find('span').get_text(strip=True)
        except:
            online = 'no data available'

        data.append({
            'name': name,
            'company': comp,
            'city': city,
            'zp': zp,
            'link': link,
            'online': online
        })

    return data


def get_vacancies(s='Python', city=40):
    params = {
        'text': s,
        'area': city
    }
    soup = get_html(URL, params=params)
    return get_content(soup=soup)


