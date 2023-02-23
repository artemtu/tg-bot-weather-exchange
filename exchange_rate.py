import requests
from bs4 import BeautifulSoup

def get_usd_info():
    URL = 'https://www.banki.ru/products/currency/cb/'
# Make a GET request to the website
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find('tr', {'data-test': 'currency-table-row'})
    info_USD = element.text.strip().split('\n')
    usd_price = float(info_USD[8])
    if usd_price > 70:
        recommendation = 'недёшево, но можно закупиться'
    elif usd_price > 80:
        recommendation = 'ждём снижения'
    elif usd_price > 100:
        recommendation = 'нам конец!'
    elif usd_price < 70:
        recommendation = 'берём бакс на все бабки!!!'
    return {
    'currency': info_USD[0],
    'price': usd_price,
    'recommendation': recommendation
    }



def get_lari_info():
    URL_lari = 'https://www.google.com/finance/quote/GEL-RUB?sa=X&ved=2ahUKEwj2rP3e9bf8AhWhSvEDHWFTBcYQmY0JegQIBhAc'
# Make a GET request to the website
    response = requests.get(URL_lari)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    element_lari = soup.find('div', {'class': 'YMlKec fxKbKc'})
    info_lari = element_lari.text.strip().split('\n')
    lari_price = float(info_lari[0])
    if lari_price > 24:
        recommendation = 'недёшево, но можно закупиться'
    elif lari_price > 27:
        recommendation = 'ждём снижения'
    elif lari_price > 30:
        recommendation = 'нам пиздец!'
    elif lari_price < 21:
        recommendation = 'берём бакс на все бабки!!!'
    return {
    'currency': 'Лари',
    'price': lari_price,
    'recommendation': recommendation
    }

lari_info = get_lari_info()
def print_lari():
    a = (f'Валюта: {lari_info["currency"]}')
    b = (f'Стоимость 1 лари (руб): {lari_info["price"]}')
    c = (f'Рекомендация к покупке: {lari_info["recommendation"]}')
    d = ('---------------------------------------------')
    return f'{a}\n{b}\n{c}\n{d}'

usd_info = get_usd_info()

def print_usd():
    a = (f'Валюта: {usd_info["currency"]}')
    b = (f'Стоимость 1$ (руб): {usd_info["price"]}')
    c = (f'Рекомендация к покупке: {usd_info["recommendation"]}')
    return f'{a}\n{b}\n{c}'

usd_final = print_usd()
lari_final = print_lari()




