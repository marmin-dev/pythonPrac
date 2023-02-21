import requests
import bs4

res = requests.get('https://quotes.toscrape.com')
soup = bs4.BeautifulSoup(res.text, 'lxml')
# # print authors
# authors = set()
# for name in soup.select(".author"):
#     authors.add(name.text)
# print(authors)

# print top ten tags
# print(soup.select('.tag-item'))
for item in soup.select('.tag-item'):
    print(item.text)
