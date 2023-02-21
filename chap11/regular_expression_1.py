text = "The agent's phone number is 408-555-1234, Call soon"
print('phone' in text)
import re

pattern = 'phone'
# 실제 색인 위치까지 리턴한다
print(re.search(pattern, text))
# pattern = 'Not In Text'
# pattern = "not in the text"
re.search(pattern,text)
match = re.search(pattern,text)
print(match.span())
# 두 메서드를 이용해서 스팬의 시작지점과 끝지점을 알 수 있다
print(match.start())
print(match.end())
print("---------")
text = 'my phone once, my phone twice'
match = re.search('phone',text)
# findall 함수는 text의 패턴처럼 일치하는 문자열을 나타내는 일치 항목의 목록을 반환한다
matches = re.findall('phone',text) # list
print(len(matches))
# 이터레이트로 찾기
for match in re.finditer('phone',text):
    print(match.span())
    print(match.group())
