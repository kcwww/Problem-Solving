# 왼쪽부터 탐색하다 , 흰돌이나 검은돌 나오면 시작
# 방향중 한곳 나오면 그 방향으로 갯수 세기
# 5개라면 종료

def go_stone(board, stone, i, j, dx, dy):
    stack = []
    r = i
    c = j
    while True:
        if not (r >= 0 and r < 19 and c >= 0 and c < 19):
            break
        if board[r][c] != stone:
            break
        stack.append([r,c])
        r = r + dx
        c = c + dy
    r = i
    c = j
    while True:
        r = r - dx
        c = c - dy
        if not (r >= 0 and r < 19 and c >= 0 and c < 19):
            break
        if board[r][c] != stone:
            break
        stack.append([r,c])
    return stack

def check_five(board,stone, i, j):
    move = [[0,1],[1,0],[-1,1],[1,1]]
    for m in move:
        r = i + m[0]
        c = j + m[1]
        if r >= 0 and r < 19 and c >= 0 and c < 19:
            if board[r][c] == stone:
                re = go_stone(board, stone, i, j, m[0], m[1])
                if re and len(re) == 5:
                    return re
    return []

board = []

import sys

for i in range(19):
    line = sys.stdin.readline().split()
    board.append(line)
re = []
r, c = 0, 0
flag = 0
for i in range(19):
    for j in range(19):
        if board[i][j] == '1' or board[i][j] == '2':
            re = check_five(board, board[i][j], i, j)
            if re and len(re) == 5:
                flag = 1
                break
    if flag == 1:
        break
if re:
    re.sort(key=lambda x : (x[1], x[0]))
    r,c = re[0][0], re[0][1]
if flag == 1:
    print(board[r][c])
    print(r + 1, c + 1)
else:
    print(0)
