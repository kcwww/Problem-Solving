import sys

N = int(sys.stdin.readline().strip())
order = sys.stdin.readline().strip()

board = []
for _  in range(N):
    board.append(['.'] * N)
nr, nc = 0,0
for o in order:
    if o == 'U':
        r = nr - 1
        if r >= 0 and r < N:
            if board[nr][nc] == '.':
                board[nr][nc] = '|'
            elif board[nr][nc] == '-':
                board[nr][nc] = '+'
            nr = r
            if board[nr][nc] == '.':
                board[nr][nc] = '|'
            elif board[nr][nc] == '-':
                board[nr][nc] = '+'
    elif o == 'D':
        r = nr + 1
        if r >= 0 and r < N:
            if board[nr][nc] == '.':
                board[nr][nc] = '|'
            elif board[nr][nc] == '-':
                board[nr][nc] = '+'
            nr = r
            if board[nr][nc] == '.':
                board[nr][nc] = '|'
            elif board[nr][nc] == '-':
                board[nr][nc] = '+'
    elif o == 'R':
        c = nc + 1
        if c >= 0 and c < N:
            if board[nr][nc] == '.':
                board[nr][nc] = '-'
            elif board[nr][nc] == '|':
                board[nr][nc] = '+'
            nc = c
            if board[nr][nc] == '.':
                board[nr][nc] = '-'
            elif board[nr][nc] == '|':
                board[nr][nc] = '+'
    elif o == 'L':
        c = nc - 1
        if c >= 0 and c < N:
            if board[nr][nc] == '.':
                board[nr][nc] = '-'
            elif board[nr][nc] == '|':
                board[nr][nc] = '+'
            nc = c

            if board[nr][nc] == '.':
                board[nr][nc] = '-'
            elif board[nr][nc] == '|':
                board[nr][nc] = '+'


for i in range(N):
    print(''.join(board[i]))
