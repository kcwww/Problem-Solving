def solution(topping):
    answer = 0
    to = {}
    for t in topping:
        if (t in to):
            to[t] += 1
        else:
            to[t] = 1
    
    bro = {}
    for t in topping:
        if (len(bro) == len(to)):
            answer += 1
        if t not in bro:
            bro[t] = 1
        else:
            bro[t] += 1
        to[t] -= 1
        if (to[t] == 0):
            del to[t]
        
        
    return answer