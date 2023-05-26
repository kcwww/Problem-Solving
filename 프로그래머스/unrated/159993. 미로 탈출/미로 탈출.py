from collections import deque

def solution(maps):
    #레버까지 최단거리 + 레버부터 출구까지 최단거리 BFS
    # 시간 초과 이유를 찾아보니 -> 방문기록을 늦게하여 중복해서 방문하는 노드 발생
    answer = 0
    move = [[1,0], [-1,0], [0,1], [0, -1]]
    row = len(maps)
    col = len(maps[0])
    
    deq = deque()
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 'S':
                start = [i,j,0]
            if maps[i][j] == 'L':
                after = [i,j,0]
    
    flag = 0
    deq.append(start)
    visited = []
    for i in range(row):
        visited.append([0] * col)
    while deq:
        x, y, cnt = deq.popleft()
        if maps[x][y] == 'L':
            answer += cnt
            flag = 1
            break
        for m in move:
            r = x + m[0]
            c = y + m[1]
            if r >= 0 and r < row and c >= 0 and c < col and visited[r][c] != 1 and maps[r][c] != 'X':
                deq.append([r,c,cnt + 1])
                visited[r][c] = 1
    if flag == 0:
        return -1
    
    deq = deque()
    deq.append([x, y, 0])
    visited = []
    flag = 0
    for i in range(row):
        visited.append([0] * col)
    while deq:
        x, y, cnt = deq.popleft()
        if maps[x][y] == 'E':
            answer += cnt
            flag = 1
            break
        for m in move:
            r = x + m[0]
            c = y + m[1]
            if r >= 0 and r < row and c >= 0 and c < col and visited[r][c] != 1 and maps[r][c] != 'X':
                deq.append([r,c,cnt + 1])
                visited[r][c] = 1
    if flag == 0:
        return -1
    return answer