s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)
# copy 복사된 객체에는 영향을 미치지 않는다
s = {1,2,3}
sc = s.copy()
print(sc)
s.add(4)
# difference
print(s.difference(sc))
# s1 과 s2사이의 차이점을 반환
s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)
print(s1)
print(s2)
# 요소 폐기
s.discard(2)
print(s)
# 교집합
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
# 서로소
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
# 서로 교집합이 없는가?
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
# 부분집합
print(s1.issubset(s2))
print(s2.issuperset(s1))
# symmetric_difference 는 두 집합의 대칭차를 반환한다
# 대칭차란 두 집합 중 하나에만 포함된 모든 요소이다/ 교집합 반대
print(s1.symmetric_difference(s2))
# 합집합
print(s1.union(s3))
# update 자신과 다른 집합의 합집합으로 집합을 업데이트한다
s1.update(s2)
s1.update(s3)
print(s1)