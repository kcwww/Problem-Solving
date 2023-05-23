def solution(dirs):
    #딕셔너리의 키값이 처음 걸은 길
    current = [0, 0]
    road = {}
    for d in dirs:
        prev = list(x for x in current)
        if d == 'U' and current[1] < 5:
            current[1] += 1
        elif d == 'D' and current[1] > -5:
            current[1] -= 1
        elif d == 'L' and current[0] > -5:
            current[0] -= 1
        elif d == 'R' and current[0] < 5:
            current[0] += 1
        else:
            continue
        s = prev + current
        s = list(str(x) for x in s)
        s = ''.join(s)
        road[s] = 1
        s = current + prev
        s = list(str(x) for x in s)
        s = ''.join(s)
        road[s] = 1
    return len(road) // 2