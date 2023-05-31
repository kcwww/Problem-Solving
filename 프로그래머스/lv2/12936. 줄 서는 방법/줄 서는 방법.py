from itertools import permutations

def factorial(number):
    if number == 1 or number == 0:
        return 1
    return number * factorial(number - 1)

def solution(n, k):
    # 4면 24 = 1 : 6 2 : 6 3 : 6 4 : 6 -> 24 6 2 1 0
    # 앞쪽서부터 넣기
    answer = []
    numbers = list(range(1, n + 1))
    print(n, k)
    while(n != 0):
        fac = factorial(n - 1)
        idx = k // fac
        k = k % fac
        if k == 0:
            answer.append(numbers.pop(idx - 1))
        else:
            answer.append(numbers.pop(idx))
        n -= 1
    
    return answer