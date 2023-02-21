# same result
import time
import timeit

start_time = time.time()
def func_one(n):
    return [str(num) for num in range (n)]

# 시간이 10 분의 1 초보다 빠르다면 결과값을 구하는데 어렵다
result = func_one(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
start_time2 = time.time()
def func_two(n):
    return list(map(str,range(n)))
result2 = func_two(1000000)
end_time2 = time.time()
elapsed_time2 = end_time2 - start_time2
print(elapsed_time2)

# timeit

stmt ='''
func_one(100)
'''
setup='''
def func_one(n):
    return [str(num) for num in range (n)]
'''
print(timeit.timeit(stmt, setup, number=100000))

stmt2='''
func_two(100)
'''
setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt2, setup2, number=100000))