from collections import deque

def solution(cards1, cards2, goal):
    ca1 = deque([c for c in cards1])
    ca2 = deque([c for c in cards2])
    for word in goal:
        if word in ca1:
            if word != ca1[0]:
                return ("No")
            ca1.popleft()
        elif word in ca2:
            if word != ca2[0]:
                return ("No")
            ca2.popleft()
        else:
            return ("No")
    answer = 'Yes'
    return answer