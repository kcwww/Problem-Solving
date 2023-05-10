def solution(s):
    answer = [0,0]
    for c in s:
        if (c == 'p' or c == 'P'):
            answer[0] += 1
        elif (c == 'y' or c == 'Y'):
            answer[1] += 1
    return answer[0] == answer[1]