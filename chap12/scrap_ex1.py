# Grabbing a Page Title
# step 1
import requests

result = requests.get('http://www.example.com')

print(type(result))
# print(result.text)

# parsing beautiful soup
# bs4를 설치하여 라이브러리를 활용하여 id, 클래스 호출, 또는 HTML태그를 통해 쉽게 얻을 수 있다

import bs4
soup = bs4.BeautifulSoup(result.text, 'lxml')

print(soup.select('title'))

print(soup.select('p'))

print(soup.select('h1'))

site_paragraphs = soup.select('p')

print(type(site_paragraphs[0]))
print(site_paragraphs[0])