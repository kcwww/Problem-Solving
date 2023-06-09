def check_block(i, j, board, m, n, stack):
    char = board[i][j]
    move = [[0, -1], [-1, 0], [-1, -1]]
    flag = 0
    for mv in move:
        r = i + mv[0]
        c = j + mv[1]
        if r >= 0 and r < m and c >= 0 and c < n:
            if char != board[r][c]:
                return
            else:
                flag += 1
    if flag == 3:
        stack.append([i,j])
    return

def delete_block(stack, board):
    re = 0
    move = [[0, 0],[0, -1], [-1, 0], [-1, -1]] 
    while stack:
        i, j = stack.pop()
        for mv in move:
            r = i + mv[0]
            c = j + mv[1]
            if board[r][c] != 0:
                board[r][c] = 0
                re += 1
    return re

def down_block(board, m, n):
    for j in range(n):
        for i in range(m - 1, -1, -1):
            if board[i][j] == 0:
                continue
            tmp = board[i][j]
            board[i][j] = 0
            r = i
            while r < m - 1 and board[r + 1][j] == 0:
                r += 1
            board[r][j] = tmp
    return

def solution(m, n, board):
    # row = m col = n
    # 모든 인덱스 순회 하면서 2x2 블록 찾기 -> 찾으면 스택에 저장 -> 스택에 있는 모든 요소 지우기
    # -> 아래로 이동후 반복
    # RMAFNTJC
    for i in range(m):
        board[i] = list(board[i])
    answer = 0
    
    while True:
        stack = []
        for i in range(m):
            for j in range(n):
                if board[i][j] != 0:
                    check_block(i, j, board, m, n, stack)
        if stack:
            answer += delete_block(stack, board)
        else:
            break
        down_block(board, m, n)
    return answer