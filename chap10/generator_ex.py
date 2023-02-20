def create_cubes(n):
    for x in range(n):
        yield x**3

# print(create_cubes(10)) return location in memory
for x in create_cubes(10):
    print(x)

def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
print(list(gen_fibon(10)))

def simple_gen():
    for x in range(3):
        yield x
for number in simple_gen():
    print(number)
g = simple_gen()
print(next(g))
print(next(g))
print(next(g))

s = 'hello'
for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))

# Extra Credit
my_list = [1,2,3,4,5]

# 리스트 컴프리헨션과 비슷하지만 메모리 목록을 새롭게 생성 하는 대신 작성한다 소괄화 주목
gencomp = (item for item in my_list if item > 3)
for item in gencomp:
    print(item)
print(gencomp)