def solution(s):
    #순회하면서 { 시작 담아주면서 , 지나가고 } 끝
    #길이 기준으로 정렬후 마지막 인덱스 리턴
    answer = []
    s = s[1:-1]
    flag = 0
    temp = ''
    for c in s:
        if (flag == 1 and c != '}'):
            temp += c
        if (c == '{'):
            flag = 1
        if (c == '}'):
            flag = 0
            answer.append(temp)
            temp = ''
    answer.sort(key=len)
    temp = []
    for a in answer:
        result = list(map(int, a.split(',')))
        for r in result:
            if r in temp:
                continue
            else:
                temp.append(r)
    return temp