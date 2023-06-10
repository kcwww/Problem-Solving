import sys

# 거북이가 F 할때마다 좌표 스택에 저장
# 다 이동을 마친후 , x 최대 최소 , y 최대 최소 구하여 넓이 구하기
# 선분일 경우는 0

TC = int(sys.stdin.readline().strip())
for i in range(TC):
    stack = [[0, 0]]
    turtle = 'N'
    x, y = 0, 0
    move = sys.stdin.readline().strip()
    
    for m in move:
        if m == 'F':
            if turtle == 'N':
                y += 1
            elif turtle == 'S':
                y -= 1
            elif turtle == 'W':
                x -= 1
            elif turtle == 'E':
                x += 1
            stack.append([x, y])
        elif m == 'B':
            if turtle == 'N':
                y -= 1
            elif turtle == 'S':
                y += 1
            elif turtle == 'W':
                x += 1
            elif turtle == 'E':
                x -= 1
            stack.append([x, y])
        elif m == 'L':
            if turtle == 'N':
                turtle = 'W'
            elif turtle == 'S':
                turtle = 'E'
            elif turtle == 'W':
                turtle = 'S'
            elif turtle == 'E':
                turtle = 'N'
        elif m == 'R':
            if turtle == 'N':
                turtle = 'E'
            elif turtle == 'S':
                turtle = 'W'
            elif turtle == 'W':
                turtle = 'N'
            elif turtle == 'E':
                turtle = 'S'
    x = sorted(stack, key=lambda x : x[0])
    y = sorted(stack, key=lambda x : x[1])
    x1, x2 = x[0][0], x[-1][0]
    y1, y2 = y[0][1], y[-1][1]
    if x1 == x2 or y1 == y2:
        print(0)
    else:
        print(abs(x1 - x2) * abs(y1 - y2))
