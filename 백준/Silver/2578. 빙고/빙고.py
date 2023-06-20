import sys

def check_cross(bingo):
    check = 0
    temp = 0
    for i in range(5):
        if bingo[i][i] == -1:
            temp += 1
    if temp == 5:
        check += 1
    temp = 0
    j = 4
    for i in range(5):
        if bingo[i][j] == -1:
            temp += 1
        j -= 1
    if temp == 5:
        check += 1
    return check

def check_line(bingo):
    check = 0
    for i in range(5):
        temp = 0
        for j in range(5):
            if bingo[j][i] == -1:
                temp += 1
        if temp == 5:
            check += 1
    for i in range(5):
        temp = 0
        for j in range(5):
            if bingo[i][j] == -1:
                temp += 1
        if temp == 5:
            check += 1
    return check

def remove_num(bingo, num):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = -1
                return
    return

def exe_bingo(bingo, answer):
    idx = 0
    for i in range(5):
        for j in range(5):
            idx += 1
            remove_num(bingo, answer[i][j])
            cross = check_cross(bingo)
            cross += check_line(bingo)
            if cross >= 3:
                return idx
    return idx

bingo = []
answer = []
for i in range(5):
    bingo.append(list(map(int, sys.stdin.readline().split())))
for i in range(5):
    answer.append(list(map(int, sys.stdin.readline().split())))

print(exe_bingo(bingo, answer))
