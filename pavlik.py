import requests
from bs4 import BeautifulSoup
import csv

max_pages = 300
before_page = 'https://franchiseforeveryone.com/index.php?lan=ru&page='
after_page = '&cou=12'

data = [['Название', 'Первоначальный взнос', 'Требуется инвестиций', 'Роялти', 'Окупаемость. Количество месяцев', 'Категория']]

for p in range(max_pages):
    url = before_page + str(p + 1) + after_page
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    ads = soup.find_all('div', class_ = "fran")

    for i in range(len(ads)):
        ad = ads[i]
            
        brand_name = ad.find('h3', class_="fran_header").text
        name_good = brand_name.replace('ï', 'i')

        div = ad.find('div', attrs={'itemprop': 'offers'})
        offers = div.find_all('span')

        first_pay = offers[0].text
        fp_wout_text = first_pay.replace('Первоначальный взнос: ', '')
        fp_good = int(fp_wout_text.replace(' $', ''))

        investition = offers[1].text
        inv_wout_text = investition.replace('Требуется инвестиций: ', '')
        inv_good = int(inv_wout_text.replace(' $', ''))

        royalty = offers[4].text
        rt_wout_text = royalty.replace('Роялти: ', '')
        try:
            rt_good = int(rt_wout_text.replace(' $', ''))
        except ValueError:
            rt_good = rt_wout_text

        time = offers[5].text
        time_good = int(time.replace('Окупаемость. Количество месяцев: ', ''))

        category = offers[6].text
        ct_good = category.replace('Категория: ', '')

        text_offers = [name_good, fp_good, inv_good, rt_good, time_good, ct_good]
        data.append(text_offers)

with open('for_pavlik.csv', 'w', newline= '') as csvfile:
    writer = csv.writer(csvfile, delimiter = ';')
    for i in data:
            writer.writerow(i)

print('все записалось!')        