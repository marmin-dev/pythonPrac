# GOAL : Get title of every book with a 2 start rating

import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
# page_num = 12
# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text,'lxml')
#
# products = soup.select('.product_pod')
# example = products[0]
# print([] == example.select(".star-rating.Two"))
# print(example.select('a')[1]['title'])
# We can check if something in 2 starts string call in, example.select(rating)
# example.select('a')[1][title]
# two_start_titles = []
two_start_titles = []
for n in range(1,51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")
    for book in books:
        # if 'star-raitng.Two' in str(book):

        if len(book.select('.start-rating.Two')) !=0:
            book_title = book.select('a')[1]['title']
            two_start_titles.append(book_title)
for title in two_start_titles:
    print(title)