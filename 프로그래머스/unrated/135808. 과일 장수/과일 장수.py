def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    idx = 0
    stack = []
    for s in score:
        stack.append(s)
        idx += 1
        if (idx == m):
            idx = 0
            answer += min(stack) * m
            stack = []
    return answer