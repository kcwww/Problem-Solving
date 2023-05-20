def solution(info, query):
    answer = []
    apply = {}

    for i in info:
        a = i.replace('and','')
        a = a.split()
        num = int(a[-1])
        
        for z in [a[0], '-']:
            for x in [a[1], '-']:
                for c in [a[2], '-']:
                    for v in [a[3], '-']:
                        str_a = ''.join([z,x,c,v])
                        if str_a in apply:
                            apply[str_a].append(num)
                        else:
                            apply[str_a] = [num]
    
    for value in apply.values():
        value.sort()
    

    for q in query:
        b = q.replace('and','')
        b = b.split()
        num = int(b[-1])
        b = ''.join(b[0:-1])
        if b in apply:
            data = apply[b]

            start = 0       
            length = len(data)
            end = length
            while start < end:
                idx = (start + end) // 2

                if (data[idx] >= num):
                    end = idx
                else:
                    start = idx + 1

            answer.append(length - start)
        else:
            answer.append(0)
    
    return answer