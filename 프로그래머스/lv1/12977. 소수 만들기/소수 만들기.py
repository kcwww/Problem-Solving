from itertools import combinations

def solution(nums):
    answer = 0
    three = list(combinations(nums, 3))
    prime = []
    for t in three:
        prime.append(sum(t))
    for p in prime:
        cnt = 0
        for i in range(1, p):
            if (p % i) == 0:
                cnt += 1
            if (cnt > 1):
                break
        if (cnt == 1):
            answer += 1
    return answer