grid = [1,2,3,4,5,6,7,8,9]
win = False
# Visualize the game
def display():
    print(grid[0] , '|' , grid[1] , '|' , grid[2])
    print('-------')
    print(grid[3] , '|' , grid[4] , '|' , grid[5])
    print('-------')
    print(grid[6] , '|' , grid[7] , '|' , grid[8])

# Choice player mark
def select_player():
    valid = True
    while valid:
        player = input('Choose O or X')
        if not player == 'O' or player == 'X':
            print("Invalid value")
        elif player == 'O':
            print('Player2 is X')
            return ('O','X')
        else:
            print('Player2 is O')
            return ('X','O')
player1, player2 = select_player()
# player1 select
def player1_turn():
    valid = True
    while valid:
        select = input("choice number 1 to 9")
        if select.isdigit() and int(select) in grid:
            change = int(select) - 1
            grid[change] = player1
            valid = not select.isdigit()
        else:
            print("invalid numb")

def player2_turn():
    valid = True
    while valid:
        select = input("choice number 1 to 9")
        if select.isdigit() and int(select) in grid:
            change = int(select) - 1
            grid[change] = player2
            valid = not select.isdigit()
        else:
            print("invalid numb")
def winner():
    # row
    win = grid[0] == grid[1] == grid[2]
    win = grid[3] == grid[4] == grid[5]
    win = grid[0] == grid[1] == grid[2]
    # col
    win = grid[0] == grid[2] == grid[6]
    win = grid[1] == grid[3] == grid[5]
    win = grid[2] == grid[4] == grid[6]
    # dia
    win = grid[2] == grid[4] == grid[6]
    win = grid[0] == grid[4] == grid[8]

while not win:
    display()
    player1_turn()
    display()
    player2_turn()
    display()
    winner()




