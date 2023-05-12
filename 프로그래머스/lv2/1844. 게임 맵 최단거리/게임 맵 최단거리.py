from collections import deque

def solution(maps):
    answer = 0
    de = deque([[0,0,1]])
    move = [[1,0], [-1,0], [0,1], [0,-1]]
    row = len(maps)
    col = len(maps[0])
    flag = 0
    while (de):
        player = de.popleft()

        for i in range(4):
            x = player[0] + move[i][0]
            y = player[1] + move[i][1]
            if (x == (row - 1) and y == (col - 1)):
                return player[2] + 1
            elif (x >= 0 and x < row and y >= 0 and y < col and maps[x][y] != 0):
                de.append([x,y,player[2] + 1])
                maps[x][y] = 0
        
    return -1