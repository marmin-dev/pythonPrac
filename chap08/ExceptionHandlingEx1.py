def add(n1,n2):
    print(n1 + n2)
try:
    add('king',20)
except:
    print("something happened")
else:
    pass
finally:
    add(len("king"),20)

# try:
#     f=open('testfile','r')
#     f.write("write a test line")
# except OSError:
#     print("Hey you have on OS Error")
#
# finally:
#     print("I always run")

# input type check method
def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Thanks")
            break
        finally:
            print("End of try/except/finally")

