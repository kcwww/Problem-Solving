def solution(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient:
        stack.append(i)
        if (i == 1):
            flag = 0
            idx = len(stack) - 2
            for i in range(3, 0, -1):
                if (idx < 0):
                    flag = 1
                    break
                if (stack[idx] != i):
                    flag = 1
                    break
                idx -= 1
            if (flag == 0):
                del stack[idx+1:idx+5]
                answer += 1
                
    return answer