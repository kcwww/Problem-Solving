from collections import deque
import sys

flag = False

def dfs(row, col, visited, maps, i, j, stack):
    global flag
    move = [[-1,1], [0,1], [1,1]]
    if flag == True:
        return
    visited[i][j] = 1
    if j == col - 1:
        flag = True
        return
    for m in move:
        r = i + m[0]
        c = j + m[1]
        if r >= 0 and r < row and c >= 0 and c < col:
            if visited[r][c] == 1 or maps[r][c] == 'x':
                continue
            dfs(row, col, visited, maps, r, c, stack)
            if flag == True:
                return
    return


row, col = map(int, sys.stdin.readline().split())

maps = []
visited = []
for _ in range(row):
    maps.append(list(sys.stdin.readline().strip()))
    visited.append([0] * col)

pipes = 0
stack = []
for i in range(row):
    flag = False
    dfs(row, col, visited, maps, i, 0, stack)
    if flag == True:
        pipes += 1

print(pipes)
