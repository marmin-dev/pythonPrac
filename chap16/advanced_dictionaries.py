d = {'k1':1,'k2':2}
d1 = {x:x**2 for x in range(10)}
print(d1)
for k in d1.items():
    print(k)
for k in d1.values():
    print(k)
for k in d1.keys():
    print(k)
