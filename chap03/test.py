# 1
st = 'Print only the words that start with s in this sentence'
stlist = st.split(' ')
print(stlist)
anslist = []
for word in stlist:
    if word[0].lower() == 's':
        anslist.append(word)
print(anslist)
print('---------------')

# 2
for evennumb in range(0,11,2):
    print(evennumb)
print('---------------')

# 3
multi3 = [x for x in range(1, 51) if x % 3 == 0]
print(multi3)
print('---------------')

# 4
str = 'Print every word in this sentence that has an even number of letters'
words = str.split(" ")
for word in words:
    if(len(word) % 2 ==0):
        print('even!')
    else:
        print(word)
print('---------------')

# 5
numbers = [x for x in range(1,101)]
for x in numbers:
    if x % 3 == 0 and x % 5 != 0:
        print('fizz')
    elif x % 3 != 0 and x % 5 == 0:
        print("buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    else:
        print(x)
# 6
strr = 'Create a list of the first letters of every word in this string'

listword = [x[0] for x in strr.split(" ")]
print(listword)
