def solution(land):
    # 깊이 우선 탐색 -> 시간 초과
    # 다이나믹 프로그래밍
    row = len(land)
    for i in range(1, row):
        for j in range(4):
            temp = 0
            for x in range(4):
                if x == j:
                    continue
                temp = max(temp, land[i - 1][x])
            land[i][j] += temp
    return max(land[row - 1])