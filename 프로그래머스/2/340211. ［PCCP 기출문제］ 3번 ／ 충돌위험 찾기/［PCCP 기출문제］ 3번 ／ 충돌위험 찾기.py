def solution(points, routes):
    answer = 0
    robots = []
    max_time = 0
    
    for route in routes:
        start = route[0] - 1
        r = points[start][0]
        c = points[start][1]
        robot = [(r, c)]
        routeLength = len(route)
        for i in range(1, routeLength):
            nextPos = route[i] - 1
            
            while r != points[nextPos][0]:
                if (r > points[nextPos][0]):
                    r -= 1
                else:
                    r += 1
                robot.append((r, c))
            
            while c != points[nextPos][1]:
                if (c > points[nextPos][1]):
                    c -= 1
                else:
                    c += 1
                robot.append((r, c))
        robots.append(robot)
        if (max_time < len(robot)):
            max_time = len(robot)
        
    for time in range(max_time):
        posCount = {}
        
        for robot in robots:
            
            if time < len(robot):
                pos = robot[time]
                
                if pos not in posCount:
                    posCount[pos] = 0
                posCount[pos] += 1
        
        for count in posCount.values():
            if count >= 2:
                answer += 1
            
        
    return answer