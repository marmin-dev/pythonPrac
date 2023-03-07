import requests
import bs4

# 특정 사이트에 리퀘스트를 보냄
req = requests.get('http://www.example.com')
print(type(req))
print(req.text) # html을 받아옴
# bs4로 파싱하여 원하는 태그를 얻을 수 있다
soup = bs4.BeautifulSoup(req.text, 'lxml')
print(soup.select('title'))
site_p_tag = soup.select('p')
print(type(site_p_tag))
print(site_p_tag[0])

import urllib.request as r
resposne = r.urlopen("https://www.google.com")
print(resposne.status)

