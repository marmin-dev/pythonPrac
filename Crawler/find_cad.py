import bs4
import requests
import tkinter as tk

def find_cad():
    a_tags = []
    input_url = input_field.get()
    text = requests.get(input_url)
    soup = bs4.BeautifulSoup(text.text, 'lxml')
    site_a_tag = soup.select('a')
    result = ''
    # print(site_a_tag)
    for link in site_a_tag:
        if 'dwg' in str(link).lower() or 'dxf' in str(link).lower() or 'cad' in str(link).lower():
            a_tags.append(link['href'])
    for a in a_tags:
        result += a + '\n'+'\n'
    if result == '':
        result = "이 버전의 한계랄까...?"
    cad_link.insert(1.0,result)

root = tk.Tk()
width = 600
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 윈도우 창 위치 계산
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

# 윈도우 창 크기 및 위치 설정
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.title("캐드 찾아주는 채댠")
# 인풋 필드
input_field = tk.Entry(root)
# 버튼
submit = tk.Button(root, text="캐드 찾기", command=find_cad)
# 헤더, URL 설명 라벨, 링크 표시 에리어, 저작권,
header = tk.Label(root, text="캐드 찾아주는 채댠")
header.config(font=("Arial",30))
des = tk.Label(root, text="아래에 주소를 입력해 주십시오")
cad_link = tk.Text(root,height=20,width=30)
copyright = tk.Label(text="COPYRIGHT.2023.03.08 BY CHAE_DA_DEUN")
copyright.config(fg="gray", font=5)

header.pack(side=tk.TOP)
des.pack(side=tk.TOP)
input_field.pack(side=tk.TOP)
submit.pack(side=tk.TOP)
cad_link.pack(side=tk.TOP)
copyright.pack(side=tk.BOTTOM)



root.mainloop()

