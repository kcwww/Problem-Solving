import sys

def get_down_side(p, ph):
    col = len(p[0])
    row = ph
    down = []
    for j in range(col - 1, -1, -1):
        for i in range(row - 1, -1, -1):
            if p[i][j] == 'X':
                down.append([i, j])
                break
    return down


def dup_lst(line):
    t = []
    for x in line:
        t.append(x)
    return t

def go_down(p, down_side):
    row = len(p)
    min_num = []


    for coor in down_side:
        r, c = coor[0], coor[1]
        height = 0
        r += 1
        while r < row:
            if p[r][c] == 'X':
                min_num.append(height)
                break
            height += 1
            r += 1

    if min_num:
        min_num = min(min_num)
    else:
        return p
    for coor in down_side:
        r, c = coor[0], coor[1]
        while r >= 0:
            if p[r][c] == 'X':
                p[r][c] = '.'
                p[r + min_num][c] = 'X'
            r -= 1
    cnt = 0
    for i in range(row):
        line = p[i]
        flag = 0
        for c in line:
            if c == 'X':
                flag = 1
        if flag == 1:
            break
        else:
            cnt += 1
    while cnt > 0:
        p.pop(0)
        cnt -= 1
    return p

plate, width, height = map(int, sys.stdin.readline().split())

answer = []
plates = []
for _ in range(plate):
    ph = int(sys.stdin.readline().strip())
    p = []
    temp = []
    for i in range(ph):
        line = list(sys.stdin.readline().strip())
        t_line = dup_lst(line)
        p.append(line)
        temp.append(t_line)
    down_side = get_down_side(p, ph)
    for i in range(len(plates)):
        p.append(plates[i])

    p = go_down(p, down_side)
    high = len(p)
    if high > height:
        answer.append(len(plates))
        plates = temp
    else:
        plates = p
answer.append(len(plates))

print(*answer)
