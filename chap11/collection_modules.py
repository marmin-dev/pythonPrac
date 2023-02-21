from collections import Counter

mylist = [1,1,1,1,2,2,2,3,3,3,3,3,3,3]
print(Counter(mylist))

mylist = ['a','a',10,10,10]
print(Counter(mylist))
# 카운터는 딕셔너리의 하위 클래스로 요소를 키로, 객체의 개수를 값으로 하는 딕셔너리이다
# 문자열만 있어도 작동한다
print(Counter('this is a real life is this a fantasy'))

mystr = 'I was born was was that was that was'
myl = mystr.split(' ')
print(Counter(myl))
c = Counter(mylist)
# 튜플 가장 많은 객체부터 나열된 튜플이다, 파라미터에 정수를
# 넣으면 가장 많은것부터 파라미터 숫자개수 까지 끊어서 리스팅한다
print(c.most_common(1))
# 리스트 타입으로 캐스팅
print(list(c))

from collections import defaultdict
d = {'a' : 1}

# 디폴트 딕셔너리는 위처럼 값이 없는 키의 딕셔너리가 호출되었을 경우 기본값을 할당하는 것이다
# 람다에 기본값을 할당한다
d = defaultdict(lambda: 0)
print(d['wrong'])

# Named Tuple
# 네임드튜플은 네임드 위치(index)를 가짐으로써 일반 튜플 객체에서 확장을 시도한다
mytuple = (10,20,30)
print(mytuple[0])
from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age = 5, breed='Husky',name='Sam')
print(type(sammy))
print(sammy)
# 마치 속성이 있는 것처럼 호출이 가능하다
print(sammy.age)