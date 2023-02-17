example = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
print(example)
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example)
print(result)
mylist = [" ","0"," "]
shuffle_list(mylist)
def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1 or 2")
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print("correct")
    else:
        print("go away")
        print(mylist)

check_guess(shuffle_list(mylist),player_guess())

def myname(name):
    print(f'hello {name}')

myname('marmin')