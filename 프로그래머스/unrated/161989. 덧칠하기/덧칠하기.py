def solution(n, m, section):
    answer = 0
    start = section[0]
    for i in section:
        if (start > i):
            continue
        elif (i > start):
            start = i
        start += m
        answer += 1
    return answer