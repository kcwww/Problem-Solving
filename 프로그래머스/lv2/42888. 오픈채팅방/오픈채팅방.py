def solution(record):
    answer = []
    uid = {}
    for r in record:
        a = r.split()
        if (a[0] == 'Enter'):
            answer.append([a[1],"님이 들어왔습니다."])
            uid[a[1]] = a[2]
        elif (a[0] == 'Leave'):
            answer.append([a[1],"님이 나갔습니다."])
        elif (a[0] == 'Change'):
            uid[a[1]] = a[2]
            continue
    
    return [uid[result[0]] + result[1]for result in answer]