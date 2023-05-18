answer = 0

def dfs(k, dungeons, visited, cnt):
    global answer
    if (cnt > answer):
        answer = cnt
    for i, dungeon in enumerate(dungeons):
        if (k >= dungeon[0] and visited[i] == 0):
            visited[i] = 1
            dfs(k - dungeon[1], dungeons, visited, cnt + 1)
            visited[i] = 0
    return

def solution(k, dungeons):
    visited = [0] * len(dungeons)
    dfs(k, dungeons, visited, 0)
    return answer