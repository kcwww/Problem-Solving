def solution(k, score):
    answer = []
    honor = []
    i = 1
    for num in score:
        honor.append(num)
        honor.sort(reverse=True)
        if i < k:
            answer.append(honor[-1])
        else:
            answer.append(honor[k - 1])
        i += 1
    return answer