# range(start, stop, step)

for num in range(10):
    print(num)
print('------------')
for num in range(3, 10):
    print(num)
print('------------')
for num in range(3, 10, 2):
    print(num)
print('------------')

# enumerate
index_count = 0
word = 'abcde'
for letter in word:
    print('At index {} the letter is {}'.format(index_count, letter))
    print(word[index_count])
    index_count += 1

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# zip
# return tuple
# 가장 짧은 리스트에 맞춰서 만들어진다
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)

# in

print(100 in mylist3)
print('a' in 'a world')
d = {'k1':345}
print(345 in d.values())

# min
# max
mylist4 = [1,2,3,4,5]
print(min(mylist4))
print(max(mylist4))

# random
from random import shuffle
# shuffle 어떤 종류의 리스트든 무작위로 섞어버린다
mylist5 = [1,2,3,4,5,6,7,8,9]
shuffle(mylist5)
print(mylist5)

# randint 무작위 정수 하나가져옴

from random import randint
print(randint(0,100))

# input

# result = input("what is your name? ")
# print(result)
# input 함수는 입력받은 모든 것을 문자열로 전달한다
# 캐스팅을 하여 사용가능하다
result = int(input('Enter Favorite numb'))
if result == 4:
    print("four")
