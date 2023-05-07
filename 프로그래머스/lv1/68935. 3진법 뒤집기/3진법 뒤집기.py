import math

def solution(n):
    number = n
    three = ''
    while (number):
        three += str(number % 3)
        number //= 3
    three = three[::-1]
    i = 0
    answer = 0
    for num in three:
        answer += math.pow(3, i) * int(num)
        i += 1
    
    return answer