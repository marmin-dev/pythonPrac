def solution(num, k):
    num1 = str(num)
    for idx,val in enumerate(num1):
        if int(val) == k:
            answer = idx+1
            break
    if not str(k) in num1:
        answer=-1
    return answer

print(solution(13295,8))