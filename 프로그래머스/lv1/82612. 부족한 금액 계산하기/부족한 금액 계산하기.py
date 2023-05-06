def solution(price, money, count):
    return  0 if (sum (i * price for i in range(1, count + 1)) - money) < 0 else sum (i * price for i in range(1, count + 1)) - money