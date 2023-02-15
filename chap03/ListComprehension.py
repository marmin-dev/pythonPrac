mystring = 'hello'
mylist = []

for letter in mystring:
    mylist.append(letter)
print(mylist)
# list comprehension
mylist2 = [letter for letter in mystring]
print(mylist2)

mylist3 = [x for x in range(20)]
print(mylist3)

mylist4 = [x**2 for x in range(20)]
print(mylist4)

#if 절 사용
mylist5 = [x for x in range(0,11) if x%2 ==0]
print(mylist5)

# 섭씨를 화씨로 계산하기
celcius = [0,10,20,34.5]
farenheit = [((9/5)*temp + 32) for temp in celcius]
print(farenheit)
# for 문으로 표현한다면
faren = []
for temp in celcius:
    faren.append(((9/5)*temp + 32))
print(faren)

# else
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

# nested loops in list comprehension
mylist = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist)

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)