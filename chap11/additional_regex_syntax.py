import re
# or operator
print(re.search(r"cat|dog","The cat is here"))

# wildcard operator
# 모든 문자에 대해 일치하는 위치를 잡는 역할을 한다
# . 는 at에 붙어있는 모든 단어를 구분하는 와일드카드 역할을 한다
# 공백도 문자열로 취급하므로 잘 선택해서 하자
list1 = re.findall(r".at","The cat in the hat sat there went splat")
print(list1)



# startswith
# ^는 검색하려는 문자열이 숫자로 시작한다는 것을 의미한다
print(re.findall(r'^\d','1 is a number'))

# endswith
# $
print(re.findall(r'\d$','number is 2'))

phrase = 'there are 3 numbers 34 inside 5 this sentence'
# 대괄호
# 숫자를 제외한 모든 객체 찾기
# 숫자가 아닌 모든 문자 하나하나가 목록으로 반환된다
pattern1 = r'[^\d]'
print(re.findall(pattern1, phrase))

# 숫자를 기준으로 끊어서 리턴
pattern2 = r'[^\d]+'
print(re.findall(pattern2, phrase))

# 구두점 제거하기
phrase2 = "This is a string! But it has punctuation. How can we remove it?"
print(re.findall(r'[^!.?]+',phrase2))
plist = re.findall(r'[^!.?]+',phrase2)
print(''.join(plist)) # 문자열 합치기

text = 'Only find the hypen-words in this sentence. But you not know how long-ish they are'
# alphanumeric
pattern3 = r'[\w]+-[\w]+'
print(re.findall(pattern3,text))