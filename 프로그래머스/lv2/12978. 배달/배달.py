from collections import deque
def dijkstra(start, distance, N, village):
    que = deque([[0, start]])
    distance[start] = 0
    while que:
        dis, now = que.popleft()
        if distance[now] < dis:
            continue
        for i in range(1, N + 1):
            if village[now][i] == 0:
                continue
            cost = dis + village[now][i]
            if distance[i] == -1 or cost < distance[i]:
                distance[i] = cost
                que.append([cost, i])
    return

def solution(N, road, K):
    answer = 0
    village = []
    distance = [-1] * (N + 1)
    for _ in range(N + 1):
        village.append([0] * (N + 1))
    for r in road:
        f, t, d = r[0], r[1], r[2]
        if village[f][t] != 0:
            d = min(village[f][t], d)
        village[f][t] = d
        village[t][f] = d
    dijkstra(1, distance, N, village)
    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1
    return answer