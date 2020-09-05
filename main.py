# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time

import bs4
import requests


class Currency:
    URL_USD = 'https://www.google.com/search?q=USD+to+RUB'
    URL_EUR = 'https://www.google.com/search?q=EUR+to+RUB'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

    # Метод для получения курса валюты
    def get_currency_price(self, url):
        # Парсим всю страницу
        full_page = requests.get(url, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = bs4.BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "DFlfde", "data-precision": 2})
        return convert[0]['data-value']

    # Проверка изменения валюты
    def check_currency(self):
        usd = float(self.get_currency_price(self.URL_USD).replace(",", "."))
        now = time.strftime("%d %b %Y %H:%M:%S", time.gmtime(time.time()))
        print(now + " ===> 1 доллар = " + str(usd))
        eur = float(self.get_currency_price(self.URL_EUR).replace(",", "."))
        print(now + " ===> 1 евро = " + str(eur))
        time.sleep(3)  # Засыпание программы на 3 секунды
        self.check_currency()


if __name__ == '__main__':
    currency_obj = Currency()
    currency_obj.check_currency()
