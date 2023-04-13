def solution(my_string):
    ms=my_string.lower()
    ma = list(ms)
    ma.sort()
    answer=''.join(ma)
    return answer
print(solution("aFBd"))