# 1
for x in range(0, 99):
    # print(99 - x)
    pass

print('-' * 10)
#2
for x in range(0,10):
    print(x * 0.1)

print('-' * 10)
# 3
for x in range(1,10):
    print(f'3 X {x} = {x*3}')

print('-' * 10)
# 4
for x in range(1,10,2):
    print(f'3 X {x} = {x*3}')

print('-' * 10)
# 5
a =0
for x in range(1,11):
    a += x
print(a)

print('-' * 10)
# 6
a =0
for x in range(1,11,2):
    a += x
print(a)

print('-' * 10)
# 7
price_list = [32100, 32150, 32000, 32500]
for x in price_list:
    print(x)
print('-' * 10)
# 8

for i, x in enumerate(price_list):
    print(i,x)

print('-' * 10)
# 9
for x in range(1,4):
    print(90 + 10 * x, price_list[i])

print('-' * 10)

# a =0
# for x in range(1,100,2):
#     a += x
# print(a)

print('-' * 10)
# 10
my_list = ["가", "나", "다", "라", "마"]

for i in range(len(my_list) - 2):
    print(my_list[i], my_list[i + 1], my_list[i + 2])

print('-' * 10)
# 11
my_list = ["가", "나", "다", "라"]
for i in range(3):
    print(my_list[3-i],my_list[2-i])

print('-' * 10)
# 12
my_list = [100, 200, 400, 800]
for i in range(3):
    print(my_list[i+1]-my_list[i])

print('-' * 10)
# 13
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list)-2):
    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)

