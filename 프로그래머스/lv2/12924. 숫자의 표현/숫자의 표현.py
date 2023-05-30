def solution(n):
    answer = 1
    start = 1
    while start < n:
        num = 0
        for i in range(start, n + 1):
            num += i
            if (num == n):
                start += 1
                answer += 1
                break
            elif (num > n):
                start += 1
                break      
    return answer