def solution(s):
    #순회하면서 { 시작 담아주면서 , 지나가고 } 끝
    #길이 기준으로 정렬후 마지막 인덱스 리턴
    answer = []
    s = s[1:-1]
    flag = 0
    temp = ''
    for c in s:
        if (c == '{'):
            flag = 1
            continue
        if (c == '}'):
            answer.append(temp)
            flag = 0
            temp = ''
            continue
        
        if (c == ',' and flag == 1):
            answer.append(temp)
            temp = ''
            continue
        elif (flag == 0):
            continue
        temp += c

    re_dict = {}
    for k in answer:
        if k in re_dict:
            re_dict[k] += 1
        else:
            re_dict[k] = 1
    re_dict = sorted(re_dict.items(), key=lambda x : -x[1])

    return [int(r[0]) for r in re_dict]