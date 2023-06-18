import sys
from collections import deque

def get_stones(r, c, board, d, stone):
    stack = []
    x = r
    y = c
    while board[x][y] == stone:
        stack.append([x, y])
        x = x + d[0]
        y = y + d[1]
        if not (x >= 0 and x < 19 and y >= 0 and y < 19):
            break
    stack.pop(0)
    x = r
    y = c
    while board[x][y] == stone:
        stack.append([x, y])
        x = x - d[0]
        y = y - d[1]
        if not (x >= 0 and x < 19 and y >= 0 and y < 19):
            break
    return stack

def check_five(r, c, board):
    stone = board[r][c]
    stones = []
    dir = [[1,1],[1,0],[0,1],[-1,1]]
    for d in dir:
        x = r + d[0]
        y = c + d[1]
        if x >= 0 and x < 19 and y >= 0 and y < 19:
            if board[x][y] == stone:
                stones = get_stones(r,c, board, d, stone)
                if len(stones) == 5:
                    return True
                else:
                    stones = []
    for d in dir:
        x = r - d[0]
        y = c - d[1]
        if x >= 0 and x < 19 and y >= 0 and y < 19:
            if board[x][y] == stone:
                stones = get_stones(r,c, board, d, stone)
                if len(stones) == 5:
                    return True
                else:
                    stones = []
    return False

N = int(sys.stdin.readline().strip())

board = []
for _ in range(19):
    board.append([0] * 19)

cnt = 0
flag = False
for _ in range(N):
    r, c = map(int, sys.stdin.readline().split())
    r, c = r - 1, c - 1
    board[r][c] = (cnt % 2) + 1
    if flag == True:
        continue
    cnt += 1
    if check_five(r,c, board):
        flag = True


if flag:
    print(cnt)
else:
    print(-1)
