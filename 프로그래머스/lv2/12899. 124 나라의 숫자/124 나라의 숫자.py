def solution(n):
    answer = ''
    flag = 0
    while n:
        num = n % 3
        if num == 0:
            flag = 1
        else:
            num = str(num)
        if flag == 1:
            n = n // 3 - 1
            num = '4'
            flag = 0
        else:
            n = n // 3
        answer = num + answer
    print(answer)
    
    return answer