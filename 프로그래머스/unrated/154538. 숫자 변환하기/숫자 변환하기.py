def solution(x, y, n):
    DP = [0 for _ in range(y + 1)]
    if (x == y):
        return 0
    for num in range(x, y+1):
        if (num != x and DP[num] == 0):
            continue
        if (num + n) <= y:
            if (DP[num + n] == 0):
                DP[num + n] = DP[num] + 1
            else:
                DP[num + n] = min(DP[num] + 1, DP[num + n])
        if (num * 2) <= y:
            if (DP[num * 2] == 0):
                DP[num * 2] = DP[num] + 1
            else:
                DP[num * 2] = min(DP[num] + 1, DP[num * 2])
        if (num * 3) <= y:
            if (DP[num * 3] == 0):
                DP[num * 3] = DP[num] + 1
            else:
                DP[num * 3] = min(DP[num] + 1, DP[num * 3])
    
    return -1 if (DP[y] == 0) else DP[y]