import sys
from collections import deque



def find_swan(lake, visited, queue):
    next_queue = deque()
    move = [[1,0], [-1,0], [0, 1], [0, -1]]
    while queue:
        y, x  = queue.popleft()
        if y == swan[1][0] and x == swan[1][1]:
            return True, None

        for m in move:
            ny = y + m[0]
            nx = x + m[1]
            if 0 <= ny < row and 0 <= nx < col and visited[ny][nx] == 0:
                if lake[ny][nx] == 'X':
                    next_queue.append((ny, nx))
                else:
                    queue.append((ny, nx))
                visited[ny][nx] = 1

    return False, next_queue

def melt_ice(water, lake):
    next_water = deque()
    move = [[1,0], [-1,0], [0, 1], [0, -1]]
    while water:
        y, x = water.popleft()
        for m in move:
            ny = y + m[0]
            nx = x + m[1]
            if 0 <= ny < row and 0 <= nx < col:
                if lake[ny][nx] == 'X':
                    next_water.append((ny, nx))
                    lake[ny][nx] = '.'
    return next_water


row, col = map(int, sys.stdin.readline().split())
lake = []
swan = []
water = deque()

for r in range(row):
    line = list(sys.stdin.readline().rstrip())
    for c in range(col):
        if line[c] == '.' or line[c] == 'L':
            water.append((r, c))
        if line[c] == 'L':
            swan.append((r, c))
    lake.append(line)

day = -1
visited = []
for _ in range(row):
    visited.append([0] * col)

queue = deque()

y, x = swan[0][0], swan[0][1]
queue.append((y, x))
visited[y][x] = 1

while True:
    day += 1
    found, next_queue = find_swan(lake, visited, queue)
    if found:
        break
    water = melt_ice(water, lake)
    queue = next_queue

print(day)
