import tkinter as tk

day = 0
month = 0
bir_m =['근','무','경','득','삼','구','창','현','평','판','달','봉']
bir_d = ['출', '걸', '필', '팔', '상', '칠', '장', '봉', '남', '태', '현', '붕', '두', '질', '귀',
         '능', '묵', '쇠', '방', '알', '동', '지', '배', '패', '록', '접', '찰', '점', '닥', '틀', '례']
# 해병대 식 이름 짓기
def marine_naming():
    input_value = input_field.get()
    input_value2 = input_field2.get()
    if input_value.isdigit() and input_value2.isdigit():
        input_value = int(input_value)
        input_value2 = int(input_value2)
        if 0 < input_value < 13 and 0< input_value2 < 32:
            result = f'악! 이병 {bir_m[input_value-1]}{bir_d[input_value2-1]}!'
        else:
            result = '기열!'
    else:
        result = "기열!"
    result_label.configure(text=result, bg='red')

window = tk.Tk()

window.title("해병대식 이름 짓기")

result_label= tk.Label(window)
month_label = tk.Label(window, text="몇 월 달에 태어났나?",bg='red')
day_label = tk.Label(window, text="몇 일 에 태어났나?",bg='red')

input_field = tk.Entry(window)
input_field2 = tk.Entry(window)
submit = tk.Button(window, text="이름 생성", command=marine_naming, bg='red')

month_label.pack(side=tk.TOP)
input_field.pack(side=tk.TOP)
day_label.pack(side=tk.TOP)
input_field2.pack(side=tk.TOP)
submit.pack(side=tk.TOP)
result_label.pack(side=tk.TOP)

window.mainloop()




