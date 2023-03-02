# 1
movie_rank = ['닥터 스트레인지','스플릿','럭키']
print(movie_rank)

# 2
movie_rank.append('배트맨')
print(movie_rank)

# 3
movie_rank.pop(2)
del movie_rank[2]
print(movie_rank)

# 4
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang3 = lang1 + lang2
print(lang3)

# 5
nums = [1,2,3,4,5,6,7]
print('max:', max(nums))
print('min:', min(nums))

# 6
nums = [1,2,3,4,5]
print(sum(nums))

# 7
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 8
nums = [1, 2, 3, 4, 5]
avg = sum(nums) / len(nums)
print(avg)

# 9
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 10
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 11
print(nums[1::2])

# 12
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

# 13
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest)) #구분자를 설정하고 뒤에 join메서드를 호출하여 문자열 형태로 반환

# 14
print("/".join(interest))

# 15
print("\n".join(interest))

# 16
string = "삼성전자/LG전자/Naver"
string = string.split("/")
print(string)

# 17
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
