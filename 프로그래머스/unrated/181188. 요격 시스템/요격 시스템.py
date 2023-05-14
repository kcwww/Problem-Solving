def solution(targets):
    targets = sorted(targets, key=lambda x : x[1])
    answer = 0
    end = 0
    for target in targets:
        if (target[0] >= end):
            answer += 1
            end = target[1]
    return answer