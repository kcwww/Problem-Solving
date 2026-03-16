from collections import deque

def solution(storage, requests):
    answer = 0
    NONE = '#'
    row = len(storage)
    col = len(storage[0])
    
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    
    for i in range(row):
        storage[i] = list(storage[i])
        
    container = [['#'] * (col + 2) for _ in range(row + 2)]
    for i in range(row):
        for j in range(col):
            container[i + 1][j + 1] = storage[i][j]
            answer += 1
    
    for request in requests:
        requestType = len(request)
        
        # 1 이면 BFS 순회
        if (requestType == 1):
            visited = [[False] * (col + 2) for _ in range(row + 2)]
            
            queue = deque([[0,0]])
            while (len(queue) > 0):
                pos = queue.popleft()
                
                visited[pos[0]][pos[1]] = True
                
                for d in direction:
                    newPosR = pos[0] + d[0]
                    newPosC = pos[1] + d[1]
                    
                    if (newPosR >= 0 and newPosR < row + 2 and newPosC >= 0 and newPosC < col + 2):
                        if (container[newPosR][newPosC] == NONE and visited[newPosR][newPosC] == False):
                            queue.append([newPosR, newPosC])
                            visited[newPosR][newPosC] = True
                        elif (container[newPosR][newPosC] == request):
                            visited[newPosR][newPosC] = True
                            container[newPosR][newPosC] = NONE
                            answer -= 1
                
            
            
        elif (requestType == 2):
        # 2 이면 그냥 지워주기
            for i in range(row):
                for j in range(col):
                    if (container[i + 1][j + 1] == request[0]):
                        container[i + 1][j + 1] = NONE
                        answer -= 1
        
        
    
    return answer