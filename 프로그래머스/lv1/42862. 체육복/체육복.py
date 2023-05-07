def solution(n, lost, reserve):

    new_lost = [x for x in lost if x not in reserve]
    new_reserve = [x for x in reserve if x not in lost]
    
    lost = sorted(new_lost)
    reserve = sorted(new_reserve)
    
    for num in reserve:
        if (num - 1) in lost:
            lost.pop(lost.index(num - 1))
        elif (num + 1) in lost:
            lost.pop(lost.index(num + 1))
        
    return n - len(lost)