# 1
apart = [[101, 102], [201, 202], [301, 302]]
print(apart)

print('-'*6)
# 2
stock = [[100,80],[200,210],[300,330]]
print(stock)

print('-'*6)
# 3

stock = {'10/10':[80,110,70,90],'10/11':[210,230,190,200]}
print(stock)

print('-'*6)
#4

apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for k in i:
        print(k , '호')

print('-'*6)
# 5

apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for k in i[::-1]:
        print(k,'호')

print('-'*6)
# 6
for i in apart:
    for k in i:
        print(k,'호')
        print('-'*5)

print('-'*6)
# 7
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for x in data:
    for d in x:
        print(d+ d*(0.014/100))

print('-'*6)
# 8

for x in data:
    for d in x:
        print(d+ d*(0.014/100))
    print('-'*3)

print('-'*6)
# 9
a = []
for x in data:
    for d in x:
        a.append(d+ d*(0.014/100))
print(a)

print('-'*6)
# 10
# a2 =[]
# a1 =[]
# for w in range(0,12,4):
#     for p in range(4):
#         a1.append(a[w+p])
#     a2.append(a1)
# print(a2)

print('-'*6)
# 11
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    print(i[3])

print('-'*6)
# 12
for i in ohlc[1:]:
    if i[3] > 150:
        print(i[3])

print('-'*6)
# 13
for i in ohlc[1:]:
    if i[3] >= i[0]:
        print(i[3])

print('-'*6)
# 14
de = []
for i in ohlc[1:]:
    de.append(i[1]-i[2])
print(de)

# 15
print('-'*6)
for i in ohlc[1:]:
    if i[3] > i[0]:
        print(i[1]-i[2])

print('-'*6)
# 16
sum = 0
for i in ohlc[1:]:
    sum += (i[3]-i[0])
print(sum)
print('-'*6)