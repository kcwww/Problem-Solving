from collections import deque
import sys

flag = False

def dfs(row, col, maps, i, j):
    global flag
    move = [[-1,1], [0,1], [1,1]]
    if flag == True:
        return
    maps[i][j] = 'x'
    if j == col - 1:
        flag = True
        return
    for m in move:
        r = i + m[0]
        c = j + m[1]
        if r >= 0 and r < row and c >= 0 and c < col:
            if maps[r][c] == 'x':
                continue
            dfs(row, col, maps, r, c)
            if flag == True:
                return
    return


row, col = map(int, sys.stdin.readline().split())

maps = []
for _ in range(row):
    maps.append(list(sys.stdin.readline().strip()))

pipes = 0
for i in range(row):
    flag = False
    dfs(row, col, maps, i, 0)
    if flag == True:
        pipes += 1

print(pipes)
