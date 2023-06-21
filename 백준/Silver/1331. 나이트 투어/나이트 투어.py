import sys

col = {'A': 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5}
move = [[-2,1],[-2,-1],[2,1],[2,-1],[1,-2],[-1,-2],[1,2],[-1,2]]
chess = []
for _ in range(6):
    chess.append([0]* 6)

night = []
for _ in range(36):
    line = sys.stdin.readline().strip()
    c = col[line[0]]
    r = 6 - int(line[1])
    night.append([r, c])

nx, ny = night[0][0], night[0][1]
idx = 1
sx, sy = nx, ny
chess[nx][ny] = 1

for i in range(1, 36):
    r, c = night[i]
    flag = 0
    for m in move:
        x = nx + m[0]
        y = ny + m[1]
        if x >= 0 and x < 6 and y >= 0 and y < 6:
            if chess[x][y] == 0 and x == r and y == c:
                nx, ny = x, y
                chess[x][y] = 1
                flag = 1
                break
    if flag == 0:
        break

if flag == 1:
    flag = 0
    for m in move:
        x = nx + m[0]
        y = ny + m[1]
        if x >= 0 and x < 6 and y >= 0 and y < 6:
            if x == sx and y == sy:
                flag = 1

if flag == 0:
    print("Invalid")
else:
    print("Valid")
