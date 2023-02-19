def display_board(board):
    print('-------')
    print(board[7] + '|'+ board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
def player_input():

    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: choose X or O')
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
player1 , player2 = player_input()

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
 pass