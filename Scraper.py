# PI-201 Mamontov Bogdan Serhiyovych V.16
# https://finance.yahoo.com/quote/BNB-USD/history?period1=1510185600&period2=1695081600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"}

url = 'https://finance.yahoo.com/quote/TRX-USD/history?period1=1510185600&period2=1695168000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

response = requests.get(url, headers=header).text

soup = BeautifulSoup(response, 'lxml')

nav_bar = soup.find_all('li', class_='nr-applet-main-nav-item Pend(navPaddings) Whs(nw) Fl(start) H(itemHeight) H(itemHeight_uhMagDesign)! Pend(30px)! closed-subnav')

dates = soup.find_all('td', class_='Py(10px) Ta(start) Pend(10px)')
info = soup.find_all('td', class_='Py(10px) Pstart(10px)')

data_list = [["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]

num = 0
for date_item in dates:
    data_list.append([
        datetime.strptime(date_item.text, "%b %d, %Y").strftime('%Y-%m-%d'),
        float(str(info[num].text).replace(",", '') if str(info[num].text).replace(",", '') != '-' else '0.0'),
        float(str(info[num + 1].text).replace(",", '') if str(info[num].text).replace(",", '') != '-' else '0.0'),
        float(str(info[num + 2].text).replace(",", '') if str(info[num].text).replace(",", '') != '-' else '0.0'),
        float(str(info[num + 3].text).replace(",", '') if str(info[num].text).replace(",", '') != '-' else '0.0'),
        float(str(info[num + 4].text).replace(",", '') if str(info[num].text).replace(",", '') != '-' else '0.0'),
        int(str(info[num + 5].text).replace(",", '') if str(info[num].text).replace(",", '') != '-' else '0'),
    ])
    num += 6

with open("my_csv.csv", "w", newline='') as file:
    csv.writer(file).writerows(data_list)
