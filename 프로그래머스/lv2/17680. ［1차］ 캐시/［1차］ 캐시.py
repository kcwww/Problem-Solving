def solution(cacheSize, cities):
    # city 모두 소문자로 초기화
    # 캐시 크기만큼 큐를 만듬
    # 큐에서 참조되었다면 가장 최근으로 다시 삽입
    # 큐에 없다면 오래된 데이터 제거후 새로운 데이터 삽입
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    size = 1
    que = []
    for city in cities:
        if city in que:
            tmp = que.index(city)
            tmp = que.pop(tmp)
            que.append(tmp)
            answer += 1
        else:
            if len(que) < cacheSize:
                que.append(city)
            else:
                que.pop(0)
                que.append(city)
            answer += 5
    return answer