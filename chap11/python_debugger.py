# 파이썬 디버거
x = [1,2,3]
y = 2
z = 3

# result = y + z
# result2 = x + y

# 파이썬 디버거 라이브러리
import pdb
result_one = y + z
# 디버거 추적 요청하기
pdb.set_trace()
result_two = y + x
# 파이썬 디버거는 기본적으로 변수를 탐색하기 위해 스크립트 중간에 일시 중지를 할 수 있게 해주므로 용이하다
# 변수가 무엇인지 파악하기 위해 print를 남발할 필요가 없다

