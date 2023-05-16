from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    q1 = sum(queue1)
    q2 = sum(queue2)
    destination = (q1 + q2) // 2
    escape = len(queue1)
    
    if (q1 + q2) % 2 != 0:
        return -1
    while q1 != destination:
        answer += 1

        if answer == (4 * escape):
            return -1
        if (q1 > q2):
            num = queue1.popleft()
            queue2.append(num)
            q1 -= num
            q2 += num
        else:
            num = queue2.popleft()
            queue1.append(num)
            q2 -= num
            q1 += num
            
    return answer