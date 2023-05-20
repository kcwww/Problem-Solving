def check_p(place, row, col):
    m = [[1,0] , [-1, 0], [0, 1], [0, -1]]
    v = [[-1,-1], [-1, 1], [1, -1], [1, 1]]
    
    for i in range(4):
        x = row + m[i][0]
        y = col + m[i][1]
        if (x >= 0 and x < 5 and y >= 0 and y < 5):
            if (place[x][y] == 'P'):
                return 0
        
    for i in range(4):
        x = row + m[i][0] * 2
        y = col + m[i][1] * 2
        if (x >= 0 and x < 5 and y >= 0 and y < 5):
            if (place[x][y] == 'P'):
                if (place[row + m[i][0]][col + m[i][1]] != 'X'):
                    return 0
    
    for i in range(4):
        x = row + v[i][0]
        y = col + v[i][1]
        if (x >= 0 and x < 5 and y >= 0 and y < 5):
            if (place[x][y] == 'P'):
                if (place[row][y] != 'X') or (place[x][col] != 'X'):
                    return 0
    
    return 1

def solution(places):
    #완전 탐색
    #P 좌표를 찾으면 2 이내의 모든 좌표 확인
    #1 이내 상하좌우 확인 -> 2 이내 상하좌우 확인 -> 이때 있으면 1이내 X확인
    #대각선 확인 -> 이때 있으면 해당 대각선 주변 확인
    answer = []
    for place in places:
        check = 1
        for i in range(5):
            for j in range(5):
                if (place[i][j] == 'P'):
                    check = check_p(place, i, j)
                if (check == 0):
                    break
            if (check == 0):
                break
        answer.append(check)
    
    return answer