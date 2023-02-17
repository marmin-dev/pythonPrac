# WARMUP SECTION
# 1
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    else:
        if a > b:
            return a
        else:
            return b
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
# Using min max func
def lesser_of_two_evens2(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)

# 2

def animal_crackers(text):
    mylist = text.lower().split(' ')
    return mylist[0][0] == mylist[1][0]

print(animal_crackers("Kendrick Lamar"))
print(animal_crackers("Rolce Royce"))

# 3
def makes_twenty(n1,n2):

    return (n1 + n2) == 20 or n1 == 20 or n2 == 20
    # if n1 == 20 or n2 == 20:
    #     return True
    # elif n1 + n2 == 20:
    #     return True
    # else:
    #     return False

print(makes_twenty(20,10))
print(makes_twenty(2,3))

print('----------------------------------')

# Level1 Problems
# 1
def old_macdonald(name):
    mylist=[]
    myname = ''
    for letter in name:
        mylist.append(letter)
    mylist[0] = mylist[0].upper()
    mylist[3] = mylist[3].upper()
    for letter in mylist:
        myname +=letter
    return myname
print(old_macdonald('macdonald'))
# solution
def old_macdonald2(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    return first_letter.upper() + inbetween + fourth_letter.upper() + rest
print(old_macdonald2('macdonald'))
# solution2
def old_macdonald3(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

print(old_macdonald3('macdonald'))
# 2
def master_yoda(text):
    mylist = text.split(" ")
    mylist = mylist[::-1]
    text1 = ''
    for word in mylist:
        text1 += word + " "
    return text1
print(master_yoda('I am home'))
print(master_yoda('We are ready'))

def master_yoda2(text):
    mylist = text.split(" ")
    mylist = mylist[::-1]
    return " ".join(mylist)
print(master_yoda2('oh shit'))
# 3
def almost_there(n):
    if (100 - 10) < n < (100 + 10):
        return True
    elif (200 - 10)< n < (200 + 10):
        return True
    else:
        return False
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
# using abs 절대값
def almost_there2(n):
    return (abs(100-n) <= 10) or (abs(200-n)<=10)
print("---------------")

# Level 2 Problems
def has_33(nums):
    i = 0
    for num in nums:
        if i == len(nums) -1:
            break
        elif nums[i] == 3 and nums[i+1] == nums[i]:
            return True
        else:
            pass
        i += 1
    return False
# solution
def has_33(nums):
    for i in range(0,len(nums)-1):
    #     if nums[i] == 3 and nums[i+1] == 3:
    #         return True
    # return False
        if nums[i:i+2] == [3,3]:
            return True
        return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# PAPER DOLL
def paper_doll(st):
    ls = []
    st3 = ''
    for letter in st:
        ls.append(letter)
    for letter in ls:
        st3 += (letter * 3)
    return st3
print(paper_doll('Hello'))

# solution

def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

def black_jack(a,b,c):
    if a + b + c <= 21:
        return sum([a, b, c])
    elif a + b + c > 21 and 11 in [a,b,c]:
        return a + b + c - 10
    else:
        return 'BUST'
print(black_jack(5,6,7))
print(black_jack(9,9,9))
print(black_jack(9,9,11))

def summer_69(arr):
    flag = True
    result = 0
    for n in arr:
        if n == 6:
            flag = False
        if flag == True:
            result += n
        elif flag == False:
            pass
        if n == 9:
            flag = True
    return result
# using while statement
def summer_692(arr):
    flag = True
    result = 0
    for n in arr:
        while flag:
            if n != 6:
                result += n
                break
            else:
                flag = False
            while not flag:
                if n != 9:
                    break
                else:
                    flag = True


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))