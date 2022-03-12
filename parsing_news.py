import requests
from bs4 import BeautifulSoup


def parsing_SportExpress():
    url = 'https://www.sport-express.ru/news/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36'}
    response = requests.get(url, headers)
    if response.status_code != 200:
        yield f'Ошибка связи с сервером'
    else:
        req = response.text
        soup = BeautifulSoup(req, 'html.parser')
        articles = soup.find_all('article', class_='se-material se-material--type-text')
        for article in articles:
            link = article.find('div', class_='se-material__title se-material__title--size-middle').a.get('href')
            sport = article.find('a').text
            title = article.find('div', class_='se-material__title se-material__title--size-middle').a.text
            yield f'Спорт:{sport}\nТайтл:{title}\nСсылка:{link}'


def parsing_SovSport():
    url = 'https://www.sovsport.ru/news'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36'}
    response = requests.get(url, headers)
    if response.status_code != 200:
        yield f'Ошибка связи с сервером'
    else:
        try:
            req = response.text
            soup = BeautifulSoup(req, 'html.parser')
            articles = soup.find_all('div', class_='item')
            for article in articles:
                title = article.find('div', class_='name').text
                sport = article.find('div', class_='sport').text
                links = article.find('a', class_='full').get('href')
                yield f'Спорт:{sport}\nТайтл:{title}\nСсылка:{links}'
        except AttributeError:
            return False


def parsing_championat():
    url = 'https://www.championat.com/news/1.html'
    url_link = 'https://www.championat.com'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        yield f'Ошибка связи с сервером!'
    else:
        req = response.text
        soup = BeautifulSoup(req, 'html.parser')
        articles = soup.find_all('div', class_='news-item')
        for article in articles:
            links = url_link + article.find('a').get('href')
            title = article.find('a').text
            yield f'Тайтл:{title}\nСсылка:{links}'

