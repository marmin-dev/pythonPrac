# Advanced Number
print(hex(1024))
print(round(5.2322,2))

# Advanced String

s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

# Advanced Sets
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.union(set2))

# Advanced Dictionaries
d = {x:x **3 for x in range(5)}
print(d)

# Advanced List
list1 = [1,2,3,4]
list1.reverse()
print(list1)
list2 = [3,4,2,5,1]
list2.sort()
print(list2)