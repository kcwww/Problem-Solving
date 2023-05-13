def solution(board):
    answer = 1
    
    
    o , x = 0, 0
    for line in board:
        for c in line:
            if (c == 'O'):
                o += 1
            elif (c == 'X'):
                x += 1
    if (o < x):
        return 0
    if (o - x > 1):
        return 0
    
    win_flag = [0,0]
    for b in board:
        if (b == 'OOO'):
            win_flag[0] = 1
        elif (b == 'XXX'):
            win_flag[1] = 1

    for i in range(3):
        if (board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[1][i] == 'O'):
            win_flag[0] = 1
        elif (board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[1][i] == 'X'):
            win_flag[1] = 1
    
    if (board[1][1] == 'O'):
        if (board[0][0] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[2][0] == 'O'):
            win_flag[0] = 1
    elif (board[1][1] == 'X'):
        if (board[0][0] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[2][0] == 'X'):
            win_flag[1] = 1
    
    if (o == x):
        if (win_flag[0] == 1):
            return (0)
    if (o > x):
        if (win_flag[1] == 1):
            return (0)
    return answer