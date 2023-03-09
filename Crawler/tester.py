import bs4
import requests
# text = requests.get('https://www.shure.com/en-MEA/products/microphones/sm57?variant=SM57-LCE')
#
# result = "주소를 확인해주세요"
# soup = bs4.BeautifulSoup(text.text, 'lxml')
# site_a_tag = soup.select('a')
#
# # print(site_a_tag)
# for link in site_a_tag:
#     if 'dwg' in str(link).lower() or 'dxf' in str(link).lower() or 'cad' in str(link).lower():
#         print(link['href'])
def find_cad():
    result = ''
    input_url = input("입력")
    text = requests.get(input_url)
    soup = bs4.BeautifulSoup(text.text, 'lxml')
    site_a_tag = soup.select('a')
    # print(site_a_tag)
    for link in site_a_tag:
        if 'dwg' in str(link).lower() or 'dxf' in str(link).lower() or 'cad' in str(link).lower():
            result += link['href']+'\n'
    return result
print(find_cad())