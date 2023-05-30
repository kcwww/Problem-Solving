def check_square(board, i, j, row, col):
    if board[i][j] == 0:
        return 0
    if i == 0:
        return board[i][j]
    if j == 0:
        return board[i][j]
    num = min(board[i - 1][j], board[i - 1][j - 1], board[i][j - 1])
    if num == 0:
        return board[i][j]
    else:
        board[i][j] = num + 1
    return board[i][j]

def solution(board):
    # 다이나믹 프로그래밍
    # 각 인덱스 위치에 정사각형의 크기 설정
    answer = 0
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            answer = max(answer, check_square(board, i, j, row, col))
    return answer ** 2