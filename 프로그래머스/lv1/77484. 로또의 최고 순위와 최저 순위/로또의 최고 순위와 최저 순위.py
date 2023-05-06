def solution(lottos, win_nums):
    answer = []
    my_score = 7
    zeros = 0
    for num in lottos:
        if (num == 0):
            zeros += 1
        elif num in win_nums:
            my_score -= 1
    answer.append(6 if my_score - zeros > 6 else my_score - zeros)
    answer.append(6 if my_score > 6 else my_score)
    return answer