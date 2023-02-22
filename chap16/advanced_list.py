l = [1,2,3]
l.append(4)
print(l)
# 요소 개수 찾기
print(l.count(10))
x = [1,2,3]
x.append([4,5])
print(x)
# 다른 리스트 요소 추가하기
x.extend([4,5])
print(x)
print(l.index(2))
# 원하는 index에 요소넣기
l.insert(2, 'inserted')
print(l)
# 파라미터에 들어있는 인덱스의 값 삭제후 반환 파라미터 없으면 마지막부터
ele = l.pop()
# 값을 찾아서 삭제하는 메서드
l.remove('inserted')
print(l)
l = [1,2,3,4,5,3]
# 중복 값일 경우 첫 번째 일치하는 값 삭제
l.remove(3)
print(l)