a = 'hello'
b = 'Hello'
c = 'this is also string'
d = "This is the 'my' cat"
print(a, '\n', b, '\n', c, '\n', d)
mystring = "Hello World"
print(mystring[0])
# H
print(mystring[-2])
mystring = 'abcdefghijk'
print(mystring[2:])
print(mystring[:2])
print(mystring[3:6])
print(mystring[::])
print(mystring[::2])

name = "sam"
# name[0] = "p" 문자열의 불변성 떄문에 재할당이 불가능하다
last_letters = name[1:]
print('P' + last_letters)
# multiple letters
letters = 'z'
print(letters * 10)

x = 'Hello World'
print(x.upper())

x = 'why you always say you love me when your high'
print(x.split('y'))

print('This is a string {}'.format("INSERTED"))

print('The {} {} {}'.format('fox','brown','quick'))

print('The {2} {1} {0}'.format('fox','brown','quick'))

print('The {f} {b} {q}'.format(f='fox',b='brown',q='quick'))


# 실수형 formatting
result = 100/777
print("The result was {}".format(result))
print("The result was {r:1.3f}".format(r=result))

name1 = 'martin'
print(f'hello, his name is {name1}')






