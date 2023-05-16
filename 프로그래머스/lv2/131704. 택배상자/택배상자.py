def solution(order):
    answer = 0
    stack = [-1]
    box = 1
    for o in order:
        while stack[-1] != o:
            stack.append(box)
            box += 1
            if (box > len(order)):
                break
        if (stack[-1] == o):
            answer += 1
            stack.pop()
        
        
    return answer