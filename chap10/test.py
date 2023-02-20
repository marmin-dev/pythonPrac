# 1
def gensquares(n):

    for x in range(n):
        yield x ** 2


for x in gensquares(10):
    print(x)

# 2
import random
random.randint(1,10)

def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)

# 3
s = 'hello'
a = iter(s)
print(next(a))