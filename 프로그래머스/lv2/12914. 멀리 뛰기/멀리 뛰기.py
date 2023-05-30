def solution(n):
    # 깊이 우선 탐색 -> 시간초과
    # 다이나믹 프로그래밍 -> n의 2칸이나 1칸전 경우의수의 합
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1234567