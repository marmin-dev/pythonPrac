# 1
print(401 / 4)
# 2
# ans = float

# 3
# **

# 4
s = 'hello'
print(s[1])
print(s[::-1])

# 5
print(s[4])
print(s[4:])
print(s[-1:])

# 6
list1 = [0, 0, 0]
list2 = [0]*3
print(list1)
print(list2)

# 7
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)
list4 = [5, 4, 3, 2, 1]
list4.sort()
print(list4)

# 8
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

dd = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(dd['k1'][0]['nest_key'][1][0])

# 9
# tuple is immutable, can't overwrite the value by using index
# list can change the value using index
# list use square brackets beside tuple use parentheses
tu = ('help','me')
print(type(tu))

print(2 > 3)
print(3 <= 2)
print(3.0 == 3)
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
print(l_one[2][0] >= l_two[2]['k1'])





