import requests
from bs4 import BeautifulSoup
from datetime import date


def get_releases():
    today = date.today()
    url = f'https://www.film.ru/soon/year/{today.year}/month/{today.month}'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36'}
    url_link = 'https://www.film.ru'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        yield f'Ошибка связи с сервером'
    else:
        res = response.text
        soup = BeautifulSoup(res, 'html.parser')
        films = soup.find_all('div', class_='film_catalog')
        for film in films:
            links = url_link + film.find('a').get('href')
            title = film.find('span', class_="film_catalog_title").strong.text
            yield f'Название фильма:{title}\nСсылка:{links}'
