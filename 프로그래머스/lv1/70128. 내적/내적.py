def solution(a, b):
    return sum(a[x] * b[x] for x in range(len(a)))