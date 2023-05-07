from itertools import combinations

def solution(numbers):
    answer = []
    a = combinations(numbers, 2)
    for i in a:
        answer.append(i[0] + i[1])
    answer = list(set(answer))
    answer.sort()
    return answer