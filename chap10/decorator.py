def func():
    return 1
print(func())
print(func)
def hello():
    return "Hello"
# greet() == hello()
greet = hello
print(greet())

del hello
# still works
print(greet())
def hello(name="Jose"):
    print('The hello() has been executed')
    # 두 함수는 hello 내부에서만 실행이 가능함 (scope is limited)
    def greet():
        return "\t This is the greet() func inside hello"

    def welcome():
        return '\t This is welcome() inside hello'

    print('I am going to return a function')

    if name == 'Jose':
        return greet
    else:
        return welcome


my_new_func = hello('Jose')
print(my_new_func())

def cool():
    def super_cool():
        return 'I am very cool'
    return super_cool()

some_func = cool()
print(some_func)

def other(some_func):
    print("other code runs here!")
    print(some_func)
other(some_func)

# decorator
def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, before the original function')
    return wrap_func()
def func_needs_decorator():
    print("I want to be decorated")

func_needs_decorator()
new_decorator(func_needs_decorator)

@new_decorator
def func_needs_decorator():
    print("I want to be decorated")

print("-----------")
def summm(original_func):
    def wrap_func():
        print("some one gave me")
        original_func()
        print("these func")
    return wrap_func()
@summm
def insert_func():
    print("somebody_helpme")

insert_func()
