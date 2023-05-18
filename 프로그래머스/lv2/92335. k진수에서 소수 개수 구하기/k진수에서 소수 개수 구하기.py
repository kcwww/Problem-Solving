def check_prime(i):
    if (i == 1):
        return 0
    elif (i == 2):
        return 1
    for n in range(2, int(i**(1/2)) + 1):
        if (i % n) == 0:
            return 0
    return (1)
        

def solution(n, k):
    answer = 0
    jin = ''
    while n:
        jin = str(n % k) + jin
        n = n // k
    a = list(str(jin).split('0'))
    for i in a:
        if (i == ''):
            continue
        answer += check_prime(int(i))
    return answer