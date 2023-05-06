def solution(absolutes, signs):
    answer = 0
    sizes = len(signs)
    for i in range(sizes):
        if signs[i] == False:
            answer -= absolutes[i]
        else:
            answer += absolutes[i]
    return answer