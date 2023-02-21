import re

text = "My phone number is 408-555-1234"
# 이스케이프 슬레시가 아닌 정규 표현식에 대한 패턴으로 사용하는 것을 파이썬에게
# 알려주기 위해서 r을 문자열 앞에 붙힌다

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)

print(phone)
print(phone.group())
print('----------')
phone2 = re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone2)
# compile 은 서로 다른 정규식 패턴 코드를 함께 컴파일 한다
# comple 함수에 입력한 모든 패턴과 반환되는 값이 일치한다
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results.group())
# index와 다르게 1부터 시작한다
print(results.group(1))