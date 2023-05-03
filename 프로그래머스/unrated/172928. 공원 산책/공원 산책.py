def find_start(park):
    i = 0
    for line in park:
        if 'S' in line:
            idx = line.index('S')
            break
        i += 1
    return [i, idx]

def mapping(park):
    row = len(park)
    col = len(park[0])
    map = [[0]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            map[i][j] = park[i][j]
    return (map)


def walking(park, routes, answer):
    row = len(park)
    col = len(park[0])
    
    dog_r = answer[0]
    dog_c = answer[1]
    
    if (routes[0] == 'E'):
        for _ in range(int(routes[2])):
            dog_c += 1
            if (dog_c >= col):
                return [-1, -1]
            elif (park[dog_r][dog_c] == 'X'):
                return [-1, -1]
    elif (routes[0] == 'W'):
        for _ in range(int(routes[2])):
            dog_c -= 1
            if (dog_c < 0):
                return [-1, -1]
            elif (park[dog_r][dog_c] == 'X'):
                return [-1, -1]
    elif (routes[0] == 'N'):
        for _ in range(int(routes[2])):
            dog_r -= 1
            if (dog_r < 0):
                return [-1, -1]
            elif (park[dog_r][dog_c] == 'X'):
                return [-1, -1]
    elif (routes[0] == 'S'):
        for _ in range(int(routes[2])):
            dog_r += 1
            if (dog_r >= row):
                return [-1, -1]
            elif (park[dog_r][dog_c] == 'X'):
                return [-1, -1]
    return ([dog_r, dog_c])

def solution(park, routes):
    answer = find_start(park)
    park = mapping(park)

    for walk in routes:
        temp = walking(park, walk, answer)
        if (temp[0] != -1):
            answer = temp

    return answer