import math
# math 라이브러리 도움말 보기
# help(math)

value = 4.35
# 내림
val1 = math.floor(value)
print(val1)
# 올림
val2 = math.ceil(value)
print(val2)
# 반올림 => 짝수나 홀수에 따라 적용되도록 선택한다
val3 = round(value)
print(val3)
# 원주율
print(math.pi)
# 공통수, 무한대나 숫자가 아님
print(math.e)
# math.nan
print(math.nan)
# 넘파이 Numpy 수치 처리를 위한 라이브러리로 공식을 많이 쓰면 쓰자
print(math.log(math.e))
print(math.log(100, 10))
print(math.sin(10))
print(math.radians(3))

# Random 라이브러리
import random
print(random.randint(0,100))
# 시드 활용하기 시드 설정을 통해 난수 생성기 사용이 가능한데, 이는 동일한 난수들이 연속으로 나타나는 것을 의미한다
random.seed(101) #유리가 원하는 임의의 값 넣기
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
# 시드를 설정한다고 랜덤 정수를 호출할 때마다 같은 값이 반환되는 것이 아니다
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))
print(random.choice(mylist))
# 복원 추출 (동일한 거 뽑기 가능)
print(random.choices(population=mylist, k=10))
# 비복원 추출
print(random.sample(population=mylist,k=10))
# 섞어잇!
random.shuffle(mylist)
print(mylist)
# 랜덤 소수
print(random.uniform(a=0,b=100))
# 가우시안 분포
print(random.gauss(mu=0,sigma=1))