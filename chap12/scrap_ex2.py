import bs4
import lxml
import requests

text = requests.get('https://en.wikipedia.org/wiki/Queen_(band)')

print(text.text)

soup_text = bs4.BeautifulSoup(text.text, 'lxml')

first_item = soup_text.select('.infobox-data')
print(first_item[0])

