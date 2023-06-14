import sys

# 각층마다 범위 설정 0, 1 비교하여
# 1초 마다 최상위 층 가능한지 체크

def go_top(stick, floor):
    man = stick[0]
    for i in range(1, floor):
        if man[0] >= stick[i][0] and man[0] <= stick[i][1]:
            man = stick[i]
        elif man[1] >= stick[i][0] and man[1] <= stick[i][1]:
            man = stick[i]
        elif man[0] <= stick[i][0] and man[1] >= stick[i][1]:
            man = stick[i]
        else:
            return True
    return False

floor, width = map(int, sys.stdin.readline().split())

floors = []
for _ in range(floor):
    a,b = map(int, sys.stdin.readline().split())
    floors.append([a,b])

stick = []
for f in floors:
    if f[1] == 0:
        stick.append([0, f[0], 0])
    else:
        stick.append([width - f[0], width, 1])


time = 0
while go_top(stick, floor):
    for s in stick:
        if s[1] - s[0] == width:
            continue
        elif s[2] == 0:
            s[0] += 1
            s[1] += 1
            if s[1] == width:
                s[2] = 1
        else:
            s[0] -= 1
            s[1] -= 1
            if s[0] == 0:
                s[2] = 0
    time += 1
print(time)
