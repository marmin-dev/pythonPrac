# 1
# hello = input("인사하세요")
# if hello == "안녕하세요":
#     print(hello*2)
# else:
#     print(hello)

# 2
# num = ''
# while not num.isdigit():
#     num = input("숫자를 입력하라")
#     if num.isdigit():
#         break
#     else:
#         print("숫자 쓰라고")
#         continue
# num=int(num)
# print(num + 10)

# 3
# al = input("문자를 입력해주세요")
# if al.isalpha():
#     if al.isupper():
#         al = al.lower()
#     else:
#         al = al.upper()
# print(al)

# 4
# money = input("돈 + 공백 + 단위")
# gadget = 0.0
# if money.endswith('달러'):
#     gadget=int(money[:-3]) * 1176
# elif money.endswith('엔'):
#     gadget=int(money[:-2]) * 1.096
# elif money.endswith('유로'):
#     gadget=int(money[:-3]) * 1268
# else:
#     gadget = int(money[:-3]) * 171
# print(gadget)

# 5
# la = []
# a = input("number1")
# la.append(a)
# a = input("number2")
# la.append(a)
# a = input("number3")
# la.append(a)
# maxi=max(la)
# print(maxi)

# 6
# phone = input("전화번호를 입력하시오")
# if phone[:3] == '011':
#     print("SKT")
# elif phone[:3] == '016':
#     print("KT")
# elif phone[:3] == '019':
#     print("LGU")
# else:
#     print("알수없음")

# 7
def fe_male(num):
    if num[7] == '1' or '3':
        print("male")
    elif num[7] == '2' or '4':
        print("female")
    else:
        print("not a human")
fe_male('990910-2233613')
# 8
def find_last(num):
    count = 2
    result = 0
    num = num.replace("-","")
    for x in num[:8]:
        result += int(x) * count
        count += 1
    count = 2
    for x in num[8:]:
        result += int(x) * count
        count +=  1
    count = result % 11
    return 11 - count
print(find_last('990810-117061'))

# 9
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")