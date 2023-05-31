import sys
from collections import deque

sys.setrecursionlimit(10000)
# 막대를 왼쪽 오른쪽 주고 받으며 던짐
# 미네랄에 부딪히면 해당칸 부서짐
# 깊이 우선 탐색으로 바닥과 붙어있는지 확인
# 연결이 안되어 있다면 클러스터의 맨 아래 행 확인하며 떨어짐
def sum_mineral(cave, R, C):
    mineral = 0
    for i in range(R):
        for j in range(C):
            if cave[i][j] == 'x':
                mineral += 1
    return mineral

def throw_stick(cave, lr, high, R, C):
    high = R - high
    if lr == 0:
        for j in range(C):
            if cave[high][j] == 'x':
                cave[high][j] = '.'
                break
    else:
        for j in range(C - 1, -1, -1):
            if cave[high][j] == 'x':
                cave[high][j] = '.'
                break
    return

flag = True

def check_cluster(cave, i, j, R, C, visited, cluster):
    global flag
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited[i][j] = 1
    if i == (R - 1):
        flag = False
    cluster.append([i, j])
    for m in move:
        x = i + m[0]
        y = j + m[1]
        if x >= 0 and x < R and y >= 0 and y < C and cave[x][y] == 'x' and visited[x][y] != 1:
            check_cluster(cave, x, y, R, C, visited, cluster)
    return

def down_cluster(cave, cluster, R, C):
    flag = True

    down_side = []
    for r, c in cluster:
        x = r + 1
        if x < R and cave[x][c] == '.':
            down_side.append([r, c])

    while flag:
        for d in down_side:
            x = d[0] + 1
            y = d[1]
            if x == R or cave[x][y] == 'x':
                flag = False
                break
        if flag == False:
            break

        for c in cluster:
            cave[c[0]][c[1]] = '.'
        for c in cluster:
            cave[c[0] + 1][c[1]] = 'x'
        for c in cluster:
            c[0] += 1
        for d in down_side:
            d[0] += 1

    return

#####################################################
R, C = map(int, sys.stdin.readline().split())
cave = [0] * R
visited = [[0] * C for _ in range(R)]
for i in range(R):
    cave[i] =list(sys.stdin.readline().strip())
stick = int(sys.stdin.readline().strip())
height = list(map(int, sys.stdin.readline().split()))
all_mineral = sum_mineral(cave, R, C)
lr = 0
while stick > 0:
    high = height.pop(0)
    throw_stick(cave, lr, high, R, C)
    all_mineral -= 1
    for i in range(R):
        for j in range(C):
            if cave[i][j] == 'x' and visited[i][j] != 1:
                flag = True
                cluster = []
                check_cluster(cave, i, j, R, C, visited, cluster)
                if flag:
                    down_cluster(cave, cluster, R, C)
                    for i in range(R):
                            for j in range(C):
                                visited[i][j] = 0

    if lr == 0:
        lr = 1
    elif lr == 1:
        lr = 0
    stick -= 1
    for i in range(R):
        for j in range(C):
            visited[i][j] = 0
for i in range(R):
    print(''.join(cave[i]))