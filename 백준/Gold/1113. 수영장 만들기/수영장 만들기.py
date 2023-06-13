from collections import deque
import sys

# bfs 탐색하여 닫힌 공간 담기
# 닫힌 공간에서 가장 큰 수 빼내고
# 닫힌 공간에서 가장 큰수를 하나 씩 증가시키며 물이 새나 dfs 확인

row , col = map(int, sys.stdin.readline().split())

def bfs_pool(high, i, j, maps):
    stack = []
    move = [[0,1], [0, -1], [1, 0], [-1, 0]]
    que = deque([[i, j]])
    row = len(maps)
    col = len(maps[0])
    visited = []
    for k in range(row):
        visited.append([0] * col)
    visited[i][j] = 1
    while que:
        x, y = que.popleft()
        if maps[x][y] > high:
            continue
        elif (x == 0 or x == row - 1 or y == 0 or y == col - 1):
            return None
        else:
            stack.append([x, y])
        for m in move:
            r = x + m[0]
            c = y + m[1]
            if r >= 0 and r < row and c >= 0 and c < col and visited[r][c] == 0:
                visited[r][c] = 1
                que.append([r, c])
    return stack

def dfs_leaks(maps, height, cd):
    move = [[0,1], [0, -1], [1, 0], [-1, 0]]
    que = deque([[cd[0], cd[1]]])
    row = len(maps)
    col = len(maps[0])
    visited = []
    for k in range(row):
        visited.append([0] * col)
    visited[i][j] = 1
    while que:
        x, y = que.popleft()
        if maps[x][y] > max_height:
            continue
        elif x == 0 or x == row - 1 or y == 0 or y == col - 1:
            return False
        for m in move:
            r = x + m[0]
            c = y + m[1]
            if r >= 0 and r < row and c >= 0 and c < col and visited[r][c] == 0:
                visited[r][c] = 1
                que.append([r, c])
    return True

maps = []
for _ in range(row):
    line = map(int, list(sys.stdin.readline().strip()))
    maps.append(list(line))

pools = []
visited = []
for _ in range(row):
    visited.append([0] * col)

for i in range(row):
    for j in range(col):
        if i == 0 or i == row - 1 or j == 0 or j == col - 1:
            continue
        if visited[i][j] == 1:
            continue
        high = maps[i][j]
        pool = bfs_pool(high, i, j, maps)
        if pool:
            for p in pool:
                visited[p[0]][p[1]] = 1
            pools.append(pool)


answer = 0
for pool in pools:
    max_height = 0
    for p in pool:
        max_height = max(max_height, maps[p[0]][p[1]])

    while dfs_leaks(maps, max_height, pool[0]):
        max_height += 1
    for p in pool:
        answer += (max_height - maps[p[0]][p[1]])
        maps[p[0]][p[1]] = max_height
print(answer)
