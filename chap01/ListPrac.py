my_list = [1,2,3]
my_list2 = ['stirng, 100, 23.2']
print(my_list)
print(len(my_list2))
mylist = ['one','two','three']
print(mylist[0])
print(mylist[1:])
another_list = ['four', 'five']
print(mylist + another_list)
new_list = mylist + another_list
new_list[0] = 'ONE ALL CAPS'
print(new_list)
new_list.append('six')
print(new_list)
new_list.pop()
print(new_list)
popped_list = new_list.pop()
print(popped_list)
print(new_list)
sorting_list = ['a','f','g','c','h']
sorting_list.sort()
my_sorted_list = sorting_list
print(my_sorted_list)
