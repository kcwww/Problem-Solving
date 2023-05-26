def solution(plans):
    answer = []
    plans.sort(key=lambda x : x[1])
    for p in plans:
        h, m = p[1].split(':')
        p[1] = int(h) * 60 + int(m)
        p[2] = int(p[2])
        
        
    current = []
    for p in plans:
        if len(current) > 0 and current[-1][1] > p[1]:
            current[-1][1] -= p[1]
        elif len(current) > 0 and current[-1][1] <= p[1]:
            answer.append(current[-1][0])
            num = p[1] - current[-1][1]
            current.pop()
            while num > 0:
                if len(current) > 0 and current[-1][1] < num:
                    answer.append(current[-1][0])
                    num = num - current[-1][1]
                    current.pop()
                elif len(current) > 0 and current[-1][1] >= num:
                    current[-1][1] -= num
                    num = 0
                    if current[-1][1] == 0:
                        answer.append(current[-1][0])
                        current.pop()
                else:
                    break
        current.append([p[0], p[1] + p[2]])
        

    for i in range(len(current)):
        sub, time = current.pop()
        answer.append(sub)
    return answer