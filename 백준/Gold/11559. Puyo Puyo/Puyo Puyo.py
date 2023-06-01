import sys
from collections import deque
# 터질수 있는 뿌요 확인 -> bfs 로 탐색후 길이 측정
# 4 이상시 동시에 터트림
# 뿌요 확인하여 내리고 반복

def init_visited(visited):
    for i in range(12):
        for j in range(6):
            visited[i][j] = 0
    return

def go_down(puyo, r, c):
    while r != 11 and puyo[r + 1][c] == '.':
        color = puyo[r][c]
        puyo[r][c] = '.'
        puyo[r + 1][c] = color
        r += 1

###########################################################
puyo = [0] * 12
visited = [0] * 12
for i in range(12):
    puyo[i] = list(sys.stdin.readline().strip())
    visited[i] = [0] * 6


move = [[0,1], [0, -1], [1,0], [-1,0]]
cnt = 0

while True:
    que = deque()
    bomb = []
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.':
                stack = []
                que.append([puyo[i][j], i, j])
                visited[i][j] = 1
                while que:
                    color , r, c = que.popleft()
                    stack.append([r,c])
                    for m in move:
                        x = r + m[0]
                        y = c + m[1]
                        if x >= 0 and x < 12 and y >= 0 and y < 6 and visited[x][y] != 1 and puyo[r][c] == puyo[x][y]:
                            que.append([color, x, y])
                            visited[x][y] = 1
                if len(stack) >= 4:
                    bomb.append(stack)
    init_visited(visited)
    if len(bomb) == 0:
        break
    for b in bomb:
        while b:
            x,y = b.pop()
            puyo[x][y] = '.'


    for i in range(11, -1, -1):
        for j in range(5, -1, -1):
            if puyo[i][j] != '.':
                go_down(puyo, i, j)

    cnt += 1

print(cnt)
