import sys

N, M = map(int, sys.stdin.readline().split())
coordinate = []
picture = []
for _ in range(101):
    picture.append([0] * 101)
for _ in range(N):
    sx, sy, ex, ey = map(int, sys.stdin.readline().split())
    for i in range(sx, ex+ 1):
        for j in range(sy, ey + 1):
            picture[i][j] += 1

cnt = 0
for i in range(101):
    for j in range(101):
        if picture[i][j] > M:
            cnt += 1
print(cnt)
