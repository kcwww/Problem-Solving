def solution(a, b, n):
    answer = 0
    while (n >= a):
        n -= a
        n += b
        answer += b
    return answer