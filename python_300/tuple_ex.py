# 1
my_variable = tuple()
print(type(my_variable))

# 2
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(type(movie_rank))

# 3
# 불가변성
# t = (1, 2, 3)
# t[0] = 'a'

# 4
t = 1, 2, 3, 4
print(type(t))
# 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작한다

# 5
t = ('a', 'b', 'c')
t = list(t)
t[0] = 'A'
t = tuple(t)
print(t, type(t))

# 6
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 7
a = tuple(range(2,99))
print(a)




