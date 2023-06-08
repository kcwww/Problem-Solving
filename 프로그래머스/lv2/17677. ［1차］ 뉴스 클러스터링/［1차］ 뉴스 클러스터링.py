from collections import deque

def solution(str1, str2):
    answer = 0
    # 교집합 / 합집합
    # 둘다 공집합이면 1
    # 중복허용 가능
    # 교집합 찾고 -> 나머지 합친거 -> 합집합
    
    # 둘다 소문자 처리
    # 2개씩 짤라서 각각의 스택에 담고
    # 같은거 비교 해서 빼내기
    # 빼낸거 -> 교집합
    # 남은거 + 빼낸거 -> 합집합
    
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = len(str1)
    s2 = len(str2)
    sd1 = []
    sd2 = []
    for i in range(s1 - 1):
        jcd = str1[i: i + 2]
        if jcd.isalpha():
            sd1.append(jcd)
    for i in range(s2 - 1):
        jcd = str2[i: i + 2]
        if jcd.isalpha():
            sd2.append(jcd)
            
    
    s1 = len(sd1)
    s2 = len(sd2)
    same = []
    sums = []
    for i in range(s1):
        for j in range(s2):
            if sd1[i] != -1 and sd1[i] == sd2[j]:
                same.append(sd1[i])
                sd1[i] = -1
                sd2[j] = -1
    for c in sd1:
        if c != -1:
            sums.append(c)
    for c in sd2:
        if c != -1:
            sums.append(c)
    if len(sums) == 0:
        return 65536
    return int(len(same) / (len(same) + len(sums)) * 65536)