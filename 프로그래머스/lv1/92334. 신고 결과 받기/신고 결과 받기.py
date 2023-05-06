def solution(id_list, report, k):
    answer = []
    
    id = {}
    k_id = {}
    for li in id_list:
        id[li] = []
        k_id[li] = 0
    
    for re in report:
        from_id, to_id = re.split()
        if to_id not in id[from_id]:
            id[from_id].append(to_id)
            k_id[to_id] += 1
    
    for i in id:
        result = 0
        for name in id[i]:
            
            if k_id[name] >= k:
                result += 1
        answer.append(result)
            
    
    return answer