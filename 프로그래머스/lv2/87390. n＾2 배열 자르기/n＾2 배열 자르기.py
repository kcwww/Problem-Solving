def solution(n, left, right):
    return list(max(x // n, x % n) + 1 for x in range(left, right + 1))