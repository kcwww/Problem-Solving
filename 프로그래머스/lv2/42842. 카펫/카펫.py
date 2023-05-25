def solution(brown, yellow):
    answer = []
    if yellow % yellow**(1/2) == 0:
        num = int((brown + yellow)**(1/2))
        answer = [num, num]
    else:
        # brown = 2x + 2(y-2)
        # yellow = (x - 2) * (y - 2) 
        # y = num - x
        # yellow = (x - 2) * (num - 2 - x) 
        # yellow = -x2 + (num - 2)x + 2x - 2*(num - 2)
        # x2 -numx + 2*(num - 2) + yellow = 0
        num = (brown // 2) + 2
        goal = 2*(num - 2) + yellow
        for i in range(2, num):
            if (i * (num - i)) == goal:
                answer.append(max(i, num - i))
                answer.append(min(i, num - i))
                break
    return answer