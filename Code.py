#имопрт библиотек
from bs4 import BeautifulSoup
import requests

#запрос к сайту
url = 'сайт например https://github.com/V0dkaDev/parser/' #Нужно вставить ваш сайт
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
response.raise_for_status()
bs = BeautifulSoup(response.text, "lxml")

#поиск нужного вам элемента
temp = bs.find('значение после первой < в строке', class_='значение которое идет после class на коде страницы')
print(temp.text.strip()) #вывод только текста
