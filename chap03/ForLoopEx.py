my_dogs = ['Mars','Frankie','Andy','Chris']

for dog in my_dogs:
    print(dog)
    print('hello')
dec = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Check for even
for num in dec:
    if(num % 2 ==0):
        print(num)
# enumerate
list_sum = 0

for num in dec:
    list_sum += num
    print(list_sum)
print(list_sum)

# String

my_string = "Hello World"
for letter in my_string:
    print(letter)

# tuple
tup = (1,2,3)
for item in tup:
    print(item)

# tuple unpacking

my_list = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in my_list:
    print(a)
    print(b)

# dictionaries

d= {'k1':1,'k2':2,'k3':3}
for item,value in d.items():
    print(item)
    print(value)