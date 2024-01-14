from bs4 import BeautifulSoup
import requests

laptops = []

for i in range(1, 21):
    response = requests.get('https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=' + str(i))
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', 'title')
    links = [str(el.get('title')) for el in links]
    laptops.extend(links)

print(laptops)