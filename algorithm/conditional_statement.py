# 1
# hello = input("인사하세요")
# if hello == "안녕하세요":
#     print(hello*2)
# else:
#     print(hello)

# 2
num = ''
while not num.isdigit():
    num = input("숫자를 입력하라")
    if num.isdigit():
        break
    else:
        print("숫자 쓰라고")
        continue
num=int(num)
print(num + 10)


