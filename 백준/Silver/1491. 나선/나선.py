import sys

c, r = map(int, sys.stdin.readline().split())
r -= 1
c -= 1
nx, ny = 0, 0
ny += c
flag = 1
dx = 0
dy = 0
while True:
    if flag == 1:
        if r == 0:
            break
        if dx == 0:
            nx += r
            dx = 1
        else:
            nx -= r
            dx = 0
        r -= 1
        flag = 0
    else:
        if c == 0:
            break
        if dy == 0:
            ny -= c
            dy = 1
        else:
            ny += c
            dy = 0
        c -= 1
        flag = 1
print(ny, nx)
