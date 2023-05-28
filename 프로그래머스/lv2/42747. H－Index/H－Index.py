def solution(citations):
    cit = sorted(citations)
    n = len(citations)
    print(cit)
    for i in range(n):
        print(cit[i], i, n, n-i)
        if cit[i] >= n-i and i < cit[i]:
            return n-i

    return 0