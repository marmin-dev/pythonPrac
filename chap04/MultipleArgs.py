def myfunc(a,b,c=0,d=0):
    # Returns 5 % of the sum of a and b
    return sum((a,b,c,d)) * 0.05
print(myfunc(40,60))

def mysum(*args):
    return sum(args) * 0.05

print(mysum(40,60,100))

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple',veggie = 'cabbage')

def myfunc(*args,**kwargs):
    print(args)
    print('I would like {} {}'.format(args[0],kwargs['food']))
myfunc(10,20,30,food='chicken', animal='dog')

def myfunc1(a):
    count = 0
    mylist = []
    st = ''
    for letter in a:
        if count % 2 == 1:
            mylist.append(letter.lower())
        else:
            mylist.append(letter.upper())
        count += 1
    for letter in mylist:
        st = st + letter
    return st

print(myfunc1('rolex'))