# function with parameters
def add_func(num1, num2):
    return num1 + num2
print(add_func(1,2))
# function without parameters
def say_hello():
    print("hello")
say_hello()
def say_hello1(name = 'default'):
    print(f"hello {name}")
say_hello1()


def high_pow(num1,num2):
    result = 1
    count = 0
    if num1 == 0:
        return 0
    if num2 == 0:
        return 1
    while count != num2:
       result *= num1
       count += 1
    return result
print(high_pow(2,10))