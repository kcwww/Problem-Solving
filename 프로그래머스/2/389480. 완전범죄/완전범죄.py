def solution(info, n, m):
    # 다이내믹 프로그래밍
    length = len(info)
    NONE = -1
    dp = [[NONE] * n for _ in range(length + 1)]
    dp[0][0] = 0
    for i in range(length):
        traceA = info[i][0]
        traceB = info[i][1]
        
        for j in range(n):
            if (dp[i][j] == NONE):
                continue
            
            # A 가 훔칠때
            nextTraceA = traceA + j
            
            if (nextTraceA < n):
                futureB = dp[i][j]
                recordedB = dp[i + 1][nextTraceA]
                if (dp[i + 1][nextTraceA] == NONE) or futureB < recordedB:
                    dp[i + 1][nextTraceA] = futureB
    
            # B 가 훔칠때
            nextTraceB = dp[i][j] + traceB
            if (nextTraceB < m):
                if (dp[i + 1][j] == NONE) or nextTraceB < dp[i + 1][j]:
                    dp[i + 1][j] = nextTraceB
            
            
    for j in range(n):
        if (dp[length][j] != NONE) and dp[length][j] < m:
            return j
            
            
    
    
    
    return -1