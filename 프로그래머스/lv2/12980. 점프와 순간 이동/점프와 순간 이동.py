def solution(n):
    ans = 0
    while n > 0:
        while n % 2 == 0:
            n //= 2
        if n > 0:
            n -= 1
            ans += 1
    return ans