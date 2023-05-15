def solution(k, tangerine):
    answer = 0
    orange = {}
    org = []
    for i in tangerine:
        if (i in orange):
            orange[i] += 1
        else:
            orange[i] = 1
            
    for key, v in orange.items():
        org.append([key,v])
    org.sort(key=lambda x : -x[1])
    
    for i in org:
        k -= i[1]
        answer += 1
        if (k <= 0):
            break
    return answer