from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque(priorities)
    li = deque(list(range(len(priorities))))
    while que:
        prior = que.popleft()
        if que and prior < max(que):
            que.append(prior)
            process = li.popleft()
            li.append(process)
        else:
            process = li.popleft()
            answer += 1
            if process == location:
                return answer
    return answer