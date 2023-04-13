def solution(board):
    for idx,row in enumerate(board):
        for idx1,p in enumerate(row):
            if p == 1:
                if idx1 != 0 or idx1 != 4:
                    if row[idx1 - 1] != 1:
                        row[idx1 - 1] = 2
                    if row[idx1 + 1] != 1:
                        row[idx1 + 1] = 2
                elif idx1 == 0:
                    if row[idx1 + 1] != 1:
                        row[idx1 + 1] = 2
                else:
                    if row[idx - 1] != 1:
                        row[idx - 1] = 2
                if idx !=0 or idx != 4:
                    if board[idx - 1][idx1] != 1:
                        board[idx - 1][idx1] = 2
                    if board[idx + 1][idx1] != 1:
                        board[idx + 1][idx1] = 2
                elif idx == 0:
                    if board[idx + 1][idx1] != 1:
                        board[idx + 1][idx1] = 2
                else:
                    if board[idx - 1][idx1] != 1:
                        board[idx - 1][idx1] = 2

    answer = 0
    for a in board:
        answer += a.count(0)
    print(board)
    return answer
# solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))