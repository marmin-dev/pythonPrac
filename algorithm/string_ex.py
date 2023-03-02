# 1
letters = 'python'
print(letters[0],letters[2])

# 2
license_plate = "24가 2210"
print(license_plate[4:])

# 3
string = "홀짝홀짝홀짝"
string = string[::2]
print(string)

# 4
phone_number = "010-1111-2222"
phone_number = phone_number.replace('-'," ")
print(phone_number)

# 5
url = "http://sharebook.kr"
li = url.split('.')
print(li[-1])

# 6
lang = 'python'

# 7
string = 'abcdfe2a354a32a'
string = string.capitalize()
print(string)

# 8
string = 'abcd'
string=string.replace('b','B') # 새로운 문자열 형태 리턴
print(string)

# 9
a = "3"
b = "4"
print(a + b)

# 10
print('-'*80)

# 11
t1 = 'python'
t2 = 'java'
print(t1 + t2)

# 12
money = "5,969,782,550"
money = money.replace(",","")
money = int(money)
print(type(money))

# 13
data = "  삼성전자  "
data = data.strip()
print(data + "22")

# 14
ticket = "for movie"
ticket = ticket.upper()
print(ticket)

# 15
hello = 'hello'
hello = hello.capitalize()
print(hello)

# 16
file_name = "xxxx.xlsx"
print(file_name.endswith('xlsx'))

# 17
file_name = "2020_연말정산.xlsx"
print(file_name.startswith('2020'))

# 18
ticker = "btc_krw_usd"
ticker = ticker.split('_')
print(ticker)

# 19
data = "03030303     "
data = data.rstrip()
print(data)

