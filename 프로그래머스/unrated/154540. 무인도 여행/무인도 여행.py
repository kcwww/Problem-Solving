import sys

sys.setrecursionlimit(10000)

def dfs(maps, i, j, temp):
    row = len(maps)
    col = len(maps[0])
    move = [[1,0], [-1,0], [0,1], [0,-1]]
    temp.append(int(maps[i][j]))
    maps[i][j] = 'X'
    
    for m in move:
        x = i + m[0]
        y = j + m[1]
        if (x >= 0 and x < row and y >= 0 and y < col and maps[x][y] != 'X'):
            dfs(maps, x, y, temp)

def solution(maps):

            
    answer = []
    temp = []
    row = len(maps)
    col = len(maps[0])
    for i in range(row):
        maps[i] = list(maps[i])
    

    for i in range(row):
        for j in range(col):
            if (maps[i][j].isdigit()):
                dfs(maps, i, j, temp)
                answer.append(sum(temp))
                temp = []
    answer.sort()
    return answer if (len(answer) > 0) else [-1]