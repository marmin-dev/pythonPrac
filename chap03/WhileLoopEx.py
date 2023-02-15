x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print("X is not less than 5")

# pass keyword

y = [1,2,3]
for item in y:
    pass
print('end of my script')

# break keyword

while x < 12:
    print(f'The current value of x is {x}')
    x += 1
    if (x == 10):
        break

# continue keyword
z = 0
while z < 12:
    z += 1
    if(z % 2 == 0):
        continue
    print(f'yeah its {z}')