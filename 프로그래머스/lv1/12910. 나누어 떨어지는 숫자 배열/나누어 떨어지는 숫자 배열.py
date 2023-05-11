def solution(arr, divisor):
    return [-1] if (len(list(i for i in arr if (i % divisor) == 0)) == 0) else list(i for i in sorted(arr) if i % divisor == 0)