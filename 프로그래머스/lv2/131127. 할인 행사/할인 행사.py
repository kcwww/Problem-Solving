def solution(want, number, discount):
    answer = 0
    want_dic = {}
    for i, n in enumerate(want):
        want_dic[n] = number[i]
    
    dis_dic = {}
    for dis in discount:
        dis_dic[dis] = 0
    
    for dis in discount[0:10]:
        dis_dic[dis] += 1
        
    
    
    idx = 10
    size = len(discount)
    for dis in discount:
        flag = 0
        for w in want_dic:
            if (w not in dis_dic):
                return 0
            if (want_dic[w] > dis_dic[w]):
                flag = 1
                break
        if (flag == 0):
            answer += 1
        if (idx >= size):
            break
        
        dis_dic[discount[idx]] += 1
        dis_dic[discount[idx - 10]] -= 1
        
        idx += 1 
        
    return answer