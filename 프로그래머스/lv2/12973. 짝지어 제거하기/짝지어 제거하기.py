from collections import deque

def solution(s):
    answer = -1
    que = deque()
    for c in s:
        if que and c == que[-1]:
            que.pop()
        else:
            que.append(c)
    return 0 if que else 1