def solution(m, musicinfos):
    answer = []
    # 기억하는 노래 구간이 끝 ~ 처음일 수 있음
    # 끊긴 경우 아닐수 있음
    # 재생 시간만큼 쭉 반복
    # 00:00 안넘김
    # 조건 일치 여러개 -> 재생 시간 제일 긴 음악 -> 이것도 같으면 먼저 입력된 음악..
    # 없을때는 (논)
    # 하나하나 비교하며 찾음 -> 찾으면 결과에 시간정보와 함께 저장 -> 최종 결과 리턴
    size = len(m)
    for music in musicinfos:
        info = list(music.split(','))
        h, mi = map(int, info[0].split(':'))
        info[0] = h * 60 + mi
        h, mi = map(int, info[1].split(':'))
        info[1] = h * 60 + mi
        answer.append(info)
    
    result = []
    for music in answer:

        playtime = music[1] - music[0]
        idx = 0
        melody = ''
        for i in range(playtime):
            melody += music[3][idx]
            idx += 1
            if music[3][idx:idx + 1] == '#':
                melody += music[3][idx]
                idx += 1
            if idx == len(music[3]):
                idx = 0

        idx = 0
        size = len(melody)
        msize = len(m)
        if msize > size:
            continue
        
        for i in range(size - msize + 1):
            if melody[i + msize : i + msize + 1] != '#' and melody[i : i + msize] == m:
                result.append([music[2], playtime])
        result.sort(key=lambda x : (-x[1]))
    return result[0][0] if result else "(None)"