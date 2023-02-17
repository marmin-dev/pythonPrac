
# ex_row = [1,2,3]
def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

# display(ex_row,ex_row,ex_row)

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]

display(row1,row2,row3)

# input 으로 사용자 입력 받기
# input("plese enter a value")
# result = input("enter here")
# print(result)

result = input("enter value")
result_int = int(result)
print(type(result_int))

# 타입 캐스팅을 할 땐 규칙대로 해야한다
# 인풋을 하면 사용자가 상호작용을 할때 까지 다음 명령이 실행되지 않는다

