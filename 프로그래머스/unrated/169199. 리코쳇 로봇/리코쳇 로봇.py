def ricochet(board, direction, r, c, walk):
    row = len(board)
    col = len(board[0])
    if direction == "UP":
        while r > 0 and board[r - 1][c] != 'D':
            r -= 1
    elif direction == "DOWN":
        while r < row - 1 and board[r + 1][c] != 'D':
            r += 1
    elif direction == "LEFT":
        while c > 0 and board[r][c - 1] != 'D':
            c -= 1
    elif direction == "RIGHT":
        while c < col - 1 and board[r][c + 1] != 'D':
            c += 1
    return [r, c, walk + 1]


def find_robot(board, row, col):
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                return [i, j, 0]

from collections import deque
            
def solution(board):
    # 로봇의 좌표 찾고
    # 밟을수 있는 좌표 visit에 저장
    # 숫자로 저장하여 해당 자리에 도착하는 최소값 설정 (중복 설정)
    # G 에 도착할때까지 모든 경로 탐색
    # BFS 탐색
    row = len(board)
    col = len(board[0])
    visited = []
    answer = -1
    for i in range(row):
        visited.append([0] * col)
    location = find_robot(board, row, col)
    direction = ["UP", "DOWN", "LEFT", "RIGHT"]
    
    deq = deque()
    deq.append(location)

    while deq:
        location = deq.popleft()
        visited[location[0]][location[1]] = 1
        r = location[0]
        c = location[1]
        walk = location[2]
        for d in direction:
            mr, mc, mw = ricochet(board, d, r, c, walk)
            if board[mr][mc] == 'G':
                return mw
            elif visited[mr][mc] == 1:
                continue 
            deq.append([mr,mc,mw])

    return answer