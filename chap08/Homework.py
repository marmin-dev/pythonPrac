try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except:
    print("Go Home")
x = 5
y = 0
try:
    z = x/y
except:
    print("Go Home")
finally:
    print("all done")

def ask():
    numb = 0
    while True:
        try:
            numb = int(input("Write a numb"))
        except:
            print("write a number")
            continue
        else:
            break
        finally:
            print(numb)
ask()