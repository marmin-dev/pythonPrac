play = True
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)
def check_():
    num1 = int(input("check the row"))
    num2 = int(input("check the column"))
    if num1 == 1:
        if num2 == 1:
            row1[0] = 'X'
        elif num2 == 2:
            row1[1] = 'X'
        elif num2 == 3:
            row1[2] = 'X'
        else:
            pass
    else:
        pass
    if num1 == 2:
        if num2 == 1:
            row2[0] = 'X'
        elif num2 == 2:
            row2[1] = 'X'
        elif num2 == 3:
            row2[2] = 'X'
        else:
            pass
    else:
        pass
    if num1 == 3:
        if num2 == 1:
            row3[0] = 'X'
        elif num2 == 2:
            row3[1] = 'X'
        elif num2 == 3:
            row3[2] = 'X'
        else:
            pass
    else:
        pass
while play:
    pass