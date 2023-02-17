# Map
def square(num):
    return num**2
my_nums = [1,2,3,4,5]
for item in map(square,my_nums):
    print(item)
mylist = list(map(square,my_nums))
print(mylist)

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
names = ['andy','sam', 'sally']
print(list(map(splicer,names)))
print('--------------')
# Filter
def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6]
print(filter(check_even,mynums))
print(list(filter(check_even,mynums)))

for n in filter(check_even,mynums):
    print(n)
print('--------------')
# Lambda Expression
print(square(3))

square1 = lambda num: num ** 2
print(square1(5))
print(list(map(lambda num:num**2,mynums)))
print(list(filter(lambda num: num % 2==0,mynums)))

sum3 = lambda num1,num2,num3 : num1 + num2 + num3
print(sum3(1,2,3))