def solution(citations):
    answer = []
    for h in range(max(citations) + 1):
        a = list(map(lambda x : x >= h, citations))
        t = a.count(True)
        f = a.count(False)
        if t >= h and f <= h:
            answer.append(h)
    return max(answer)