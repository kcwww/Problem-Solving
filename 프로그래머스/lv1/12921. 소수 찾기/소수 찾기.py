def solution(n):
    re = 0
    answer = list(range(2, n + 1))
    for num in answer:
        if (num % 2) == 0 and num != 2:
            continue
        elif (num % 3) == 0 and num != 3:
            continue
        elif (num % 5) == 0 and num != 5:
            continue
        elif (num % 7) == 0 and num != 7:
            continue
        else:
            cnt = 0
            for i in range(2, int(num**(1/2)) + 1):
                if (num % i) == 0:
                    cnt += 1
                    break
            if (cnt == 0):
                re += 1
    return re