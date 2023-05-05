from collections import Counter

def solution(X, Y):
    answer = ''
    x = Counter(X); y = Counter(Y)

    for left in x:
        cnt = 0
        if left in y:
            cnt = min(x[left], y[left])
        for right in range(cnt):
            answer += left

    if answer == '':
        return "-1"
    else:
        answer = sorted(answer, reverse=True)
        if answer[0] == '0':
            return '0'

    return ''.join(answer)