def solution(players, m, k):
    # 시간대 24개의 배열을 만들어서 배열마다 서버를 채워놓자.
    # 서버가 증설 될때 answer += 1
    # 서버는 n x m 이상 (n + 1) x m 미만이라면 최소 n 대의 증설된 서버가 운영 중
    # 서버는 한번 증설될때, K 시간만큼 운영
    answer = 0
    servers = [0] * 24
    length = len(players)
    
    for i in range(length):
        currentServer = servers[i]
        player = players[i]
        
        required = player // m
        lack = required - currentServer
        if (lack > 0):
            answer += lack
            currentTime = i
            for _ in range(k):
                if (currentTime >= 24): break
                servers[currentTime] += lack
                currentTime += 1
    
    
        
    
    return answer