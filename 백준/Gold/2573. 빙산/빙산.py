from collections import deque
import sys

def melt_ice(ice, visited, row, col, i, j, water):
    move = [[1,0],[-1,0],[0,-1],[0,1]]
    que = deque([[i,j]])
    visited[i][j] = 1
    while que:
        x, y = que.popleft()
        for m in move:
            r = x + m[0]
            c = y + m[1]
            if r >= 0 and r < row and c >= 0 and c < col:
                if ice[r][c] != 0 and visited[r][c] == 0:
                    visited[r][c] = 1
                    que.append([r, c])
                if ice[r][c] == 0:
                    water[x][y] += 1
    for k in range(row):
        for m in range(col):
            if water[k][m] != 0:
                ice[k][m] -= water[k][m]
                if ice[k][m] < 0:
                    ice[k][m] = 0
                water[k][m] = 0
    return

def check_ice(ice, visited, row, col, water):
    year = 0
    while True:
        cnt = 0
        for i in range(row):
            for j in range(col):
                if visited[i][j] == 0 and ice[i][j] != 0:
                    if cnt == 0:
                        melt_ice(ice, visited, row, col, i, j, water)
                        cnt += 1
                    else:
                        return year
        if cnt == 0:
            return 0
        year += 1
        for i in range(row):
            for j in range(col):
                visited[i][j] = 0
    return 0

row, col = map(int, sys.stdin.readline().split())

ice = []
visited = []
water = []
for _ in range(row):
    line = list(map(int, sys.stdin.readline().split()))
    ice.append(line)
    visited.append([0] * col)
    water.append([0] * col)

print(check_ice(ice, visited, row, col, water))
