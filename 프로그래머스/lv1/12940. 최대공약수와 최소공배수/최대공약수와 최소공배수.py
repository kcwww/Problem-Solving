def solution(n, m):
    answer = []
    n1 = []
    n2 = []
    for i in range(1, n + 1):
        if (n % i) == 0:
            n1.append(i)
    for i in range(1, m + 1):
        if (m % i) == 0:
            n2.append(i)
    
    same_y = []
    for i in n1:
        for j in n2:
            if i == j:
                same_y.append(i)
    answer.append(max(same_y))
    
    nm = n * m
    n1 = []
    for i in range(n, nm + 1, n):
        n1.append(i)
    n2 = []
    for i in range(m, nm + 1, m):
        n2.append(i)
    
    same_y = []
    for i in n1:
        for j in n2:
            if (i == j):
                same_y.append(i)
                break
                            
    answer.append(min(same_y))
    return answer