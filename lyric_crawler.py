import asyncio
import bs4
import requests
from bs4 import BeautifulSoup


async def get_lyric():
    request_url = 'https://open.spotify.com/track/7GNRUsU3M4XNDDB9xle5Dz'

    # HTTP GET 요청 보내기
    response = requests.get(request_url)

    # 응답의 HTML 내용을 BeautifulSoup으로 파싱
    soup = BeautifulSoup(response.content, 'html.parser')

    # 클래스가 'Type__TypeElement-sc-goli3j-0 bGcjcI xt5C47eHPYNiriMJxGnC'인 요소 가져오기
    lyric_element = await soup.find('p', {'class': 'Type__TypeElement-sc-goli3j-0 bGcjcI xt5C47eHPYNiriMJxGnC'})

    # 요소의 텍스트 가져오기
    lyric = lyric_element.text if lyric_element else None

    return lyric

print(get_lyric())


# 크롤링 메서드 실행
lyric = asyncio.run(get_lyric())
print(lyric)