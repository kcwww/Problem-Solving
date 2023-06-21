import sys

def check_other(robots, robot):
    idx = 0
    for r in robots:
        if idx == robot:
            idx += 1
            continue
        if r[0] == robots[robot][0] and r[1] == robots[robot][1]:
            print("Robot", robot + 1, "crashes into robot", idx + 1)
            return True
        idx += 1
    return False

def operation(robots, oper, row, col):
    direction = { 'E' : [0, 1, 0], 'S' : [1, 0, 1], 'W' : [0, -1, 2], 'N' : [-1, 0, 3] }
    dir4 = ['E', 'S', 'W', 'N']
    for o in oper:
        robot, order, repeat  = o[0], o[1], o[2]
        dir = direction[robots[robot][2]]
        didx = dir[2]
        if order == 'F':
            for _ in range(repeat):
                x = robots[robot][0] + dir[0]
                y = robots[robot][1] + dir[1]
                if x >= 0 and x < row and y >= 0 and y < col:
                    robots[robot][0] = x
                    robots[robot][1] = y
                    if check_other(robots, robot):
                        return
                else:
                    print("Robot",robot + 1,"crashes into the wall")
                    return
        elif order == 'L':
            for _ in range(repeat):
                didx -= 1
                if didx < 0:
                    didx = 3
            robots[robot][2] = dir4[didx]
        elif order == 'R':
            for _ in range(repeat):
                didx = (didx + 1) % 4
            robots[robot][2] = dir4[didx]
    print('OK')


col, row = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())

robots = []
for _ in range(N):
    y, x, dir = sys.stdin.readline().split()
    x, y = row - int(x), int(y) - 1
    robots.append([x,y,dir])



oper = []
for _ in range(M):
    r_idx, op, repeat = sys.stdin.readline().split()
    r_idx, repeat = int(r_idx) - 1, int(repeat)
    oper.append([r_idx, op, repeat])


operation(robots, oper, row, col)
