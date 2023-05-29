def solution(n):
    answer = ''

    while n:
        num = n % 3
        if num == 0:
            n = n // 3 - 1
            num = '4'
        else:
            n = n // 3
            num = str(num)          
        answer = num + answer
    return answer