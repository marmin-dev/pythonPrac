s = 'hello world'
# 첫번째 문자 대문자화
s.capitalize()
# 전체 대/소문자화
s.upper()
s.lower()
# 문자 개수리턴
s.count('o')
# 문자가 위치한 인덱스 리턴
s.find('o')
# 원래 문자열을 가운데에 두고 나머지를 파라미터에 지정한 스트링으로 채움
s.center(20,'z')
# escape sequence는 구문분석(파싱)시에 사용한다
s = 'hello'
# s에 할당된 문자가 모두 영숫자인지 확인한다
print(s.isalnum())
# 모두 알파벳인지 인
print(s.isalpha())
# 모두 소문자인지 확인
s.islower()
# 빈공간인지 확인
s.isspace()

# 정규 표현식 연산
# 모든 e를 분리하여 리스트로 반환
print(s.split('e'))
# 첫번쨰 구분자 분리, 첫번쟤 두번째 세번째로 분리
s.partition()