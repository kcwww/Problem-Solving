import math

def divisor(num):
    if (num == 1):
        print(num, 1)
        return 1
    sq = math.sqrt(num)
    result = 0
    for i in range(1, int(sq) + 1):
        if (num % i) == 0:
            result += 1
    if (num % sq) == 0:
        result = result * 2 - 1
    else :
        result *= 2
    return result

def get_weapon(num, limit, power):
    weapon = divisor(num)
    if (weapon > limit):
        weapon = power
    return weapon
    
def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        answer += get_weapon(i, limit, power)
    return answer