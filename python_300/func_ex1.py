# 1
def print_bit():
    print('BitCoin')
print_bit()

print('-'*6)
# 2
def bit_100():
    for x in range(101):
        print_bit()

# 3
def print_with_smile(st):
    print(st,':D')
print_with_smile("헤헤")

print('-'*6)
# 4
def print_upper_price(price):
    if str(type(price)) == "<class 'int'>":
        print(price*1.3)
    else:
        print("숫자 해라")
print_upper_price(1000)

print('-'*6)
# 5
def print_arithmetic_operation(n1, n2):
    print(n1+n2)
    print(n1 - n2)
    print(n1 * n2)
    print(n1/n2)

print('-'*6)

# 6
print('-'*6)

def print_max():
    nl =[]
    n1 = int(input("num"))
    nl.append(n1)
    n1 = int(input("num"))
    nl.append(n1)
    n1 = int(input("num"))
    nl.append(n1)
    print(max(nl))
# print_max()

# 7
print('-'*6)

def print_reverse(st):
    print(st[::-1])
# print_reverse('rolex')

def avg_li(li):
    print(sum(li)/len(li))
# avg_li([1,2,3])

def print_even(li):
    for x in li:
        if x % 2 ==0:
            print(x)
ds = {}

def print_keys(di):
    k1=di.keys()
    for k in k1:
        print(k)
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_keys(d,k):
    print(d[k])
# print_value_by_keys(my_dict, "10/26")

import math
def print_5xn(st):
    for i in range(math.ceil((len(st)/5))):
        print(st[i*5 : i*5+5])



def print_3xn(st):
    for i in range(math.ceil((len(st)/3))):
        print(st[i*3 : i*3+3])
# print_3xn("아이엠어보이유얼어걸")

def make_url(st):
    return "www."+st+".com"
print(make_url("naver"))

def pickup_even(li):
    even = [x for x in li if x %2 ==0]
    return even
print(pickup_even([3, 4, 5, 6, 7, 8]))

# import time
#
# def time_it(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Elapsed time: {end - start}")
#         return result
#     return wrapper
#
# @time_it
# def my_func():
#     # do some time-consuming task
#     time.sleep(2)
#
# my_func()

def convert_int(st):
    st = int(st.replace(',',""))
    return st
print(convert_int("1,234,567"))


