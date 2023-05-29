def solution(n):
    a, b = 2, 3

    for i in range(3, n):
        a, b = b, a + b
    
    return a if n == 2 else (b % 1000000007)