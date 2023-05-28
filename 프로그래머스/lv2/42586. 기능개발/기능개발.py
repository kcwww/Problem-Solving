from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        day = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            day += 1
        answer.append(day)
                
    return answer