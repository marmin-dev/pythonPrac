# testing scope

x = 25
def printer():
    x=50
    return x
print(x)
print(printer())

name = "This is global string"

# def greet():
#     # Enclosing
#     name:"Sammy"
#     def hello():
#         # Local
#         print('Hello'+name)
#     hello()
# greet()

y = 50
def func():
    global y
    print(f'x is {y}')

    # LOCAL REASSIGNMENT: ON A GLOBAL VARIABLE
    y = 200
    print(f'x is {y}')

