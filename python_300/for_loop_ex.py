# 1
for x in [10,20,30]:
    print(x)

print('-'*10)

# 2
for x in [100,200,300]:
    print(x + 10)
print('-'*10)

# 3
cor = ["SK하이닉스", "삼성전자", "LG전자"]
for x in cor:
    print(len(x))
print('-'*10)

# 4
animals = ['dog', 'cat', 'parrot']
for x in animals:
    print(x[0])
print('-'*10)

# 5
kr = ["가", "나", "다", "라"]
for x in kr[::2]:
    print(x)

print('-' * 10)
# 6

for x in kr[::-1]:
    print(x)

print('-' * 10)
# 7
for x in [3, 100, 23, 44]:
    if x % 3==0:
        print(x)
print('-' * 10)
# 8
for x in [13, 21, 12, 14, 30, 18]:
    if x < 20:
        if x % 3 ==0:
            print(x)

print('-' * 10)
# 9
for x in ["I", "study", "python", "language", "!"]:
    if len(x) >= 3:
        print(x)

print('-' * 10)
# 10
for x in ["A", "b", "c", "D"]:
    if x.isupper():
        print(x)

print('-' * 10)
# 11
for x in ['dog', 'cat', 'parrot']:
    print(x.capitalize())

print('-' * 10)
# 12
for x in ['hello.py', 'ex01.py', 'intro.hwp']:
    print(x.split('.')[0])

print('-' * 10)
# 13
for x in ['intra.h', 'intra.c', 'define.h', 'run.py']:
    if x.endswith('h'):
        print(x)

print('-' * 10)
# 14
for n in range(2002,2051,4):
    print(n)

print('-' * 10)
# 15
for n in range(1,31):
    if n % 3 ==0:
        print(n)
print('-' * 10)