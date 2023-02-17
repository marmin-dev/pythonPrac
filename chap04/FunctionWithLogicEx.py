# find even numbers
def check_even(num1):
    if num1 % 2 == 1:
        return False
    else:
        return True
def even_check(number):
    result = number % 2 == 0
    return result
print(check_even(23))
print(check_even(23))

# Return True if Any number is Even Inside a List
def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False
print(check_even_list([1,3,5,7,8]))

# return all even numbers inside a list

def return_even_number(num_list):
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            pass
    return even_list

print(return_even_number([1,3,5,6,78,9]))

