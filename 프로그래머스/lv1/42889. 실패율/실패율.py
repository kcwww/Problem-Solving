def solution(N, stages):
    re = {}
    
    for i in range(1,N+1):
        re[i] = 0
    
    for i in range(N, 0, -1):
        deno = 0
        numer = 0
        for num in stages:
            if (i <= num):
                deno += 1
            if (i == num):
                numer += 1
        if (deno == 0):
            continue
        re[i] = numer / deno
    
    answer = []
    for var in re:
        answer.append(re[var])
    
    answer.sort(reverse=True)
    result = []

    for a in answer:
        for num in re:
            if (re[num] == a):
                result.append(num)
                re[num] = -1
                break
    
    return result