def solution(n, words):
    idx = 0
    answer = [0, 0]
    stack = []
    for w in words:
        if w in stack:
            answer[0] = idx % n + 1
            answer[1] = idx // n + 1
            break
        elif stack and stack[-1][-1] != w[0]:
            answer[0] = idx % n + 1
            answer[1] = idx // n + 1
            break
        else:
            stack.append(w)
        idx += 1
    return answer