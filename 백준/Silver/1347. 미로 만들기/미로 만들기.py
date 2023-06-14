from collections import deque
import sys

N = int(sys.stdin.readline().strip())
move = sys.stdin.readline().strip()
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
hongjun = [0, 0]
stack = [[0, 0]]
d = 0
for i in range(N):
    if move[i] == 'R':
        if d == 0:
            d = 3
        else:
            d -= 1
    elif move[i] == 'L':
        d = (d + 1) % 4
    elif move[i] == 'F':
        r = hongjun[0] + direction[d][0]
        c = hongjun[1] + direction[d][1]
        if r < 0:
            for st in stack:
                st[0] = st[0] + 1
            r += 1
        elif c < 0:
            for st in stack:
                st[1] = st[1] + 1
            c += 1
        stack.append([r, c])
        hongjun = [r, c]

row = max(x[0] for x in stack)
col = max(x[1] for x in stack)
miro = []
for i in range(row + 1):
    line = []
    for j in range(col + 1):
        line.append('#')
    miro.append(line)

while stack:
    x, y = stack.pop()
    miro[x][y] = '.'

for i in range(row + 1):
    print(''.join(miro[i]))
