# num = 'q'
# while not num.isdigit():
#     num = input('숫자 입력')
#     if not num.isdigit():
#         print(f"{num}는 숫자가 아닙니다")
#         continue
# i = 0
# num = int(num)
# while i < num:
#     i += 1
#     print(num)
def printer(num):
    i = 0
    while i < num:
        i += 1
        print(num)

def validate_num():
    while True:
        try:
            num = int(input("숫자를 입력하세요"))
        except ValueError:
            print("숫자가 아닙니다")
            continue
        break
    return num

printer(validate_num())
