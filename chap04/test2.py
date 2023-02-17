# CHALLENGING PROBLEMS
# 1
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
            continue
        else:
            pass
    return len(code) == 1
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# def count_primes(num):
#     primes = [2]
#     x = 3
#     if num < 2:
#         return 0
#     while x <= num:
#         for y in range(3,x,2):
#             if x % y == 0:
#                 x += 2
#                 break
#             else:
#                 primes.append(x)
#                 x += 2
#     print(primes)
#     return len(primes)
#
# count_primes(100)

def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
            else:
                primes.append(x)
                break
    print(primes)
    return len(primes)
print(count_primes2(100))