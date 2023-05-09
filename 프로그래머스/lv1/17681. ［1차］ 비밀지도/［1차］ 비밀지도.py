def solution(n, arr1, arr2):
    answer = []
    
    ar1 = []
    for one in arr1:
        a1 = ''
        while one:
            a1 = str(one % 2) + a1
            one //= 2
        while (len(a1) < n):
            a1 = '0' + a1
        ar1.append(a1)
    
    ar2 = []
    for two in arr2:
        a2 = ''
        while two:
            a2 = str(two % 2) + a2
            two //= 2
        while (len(a2) < n):
            a2 = '0' + a2
        ar2.append(a2)
        
    for i in range(n):
        re = ''
        for j in range(n):
            if (ar1[i][j] == '1' or ar2[i][j] == '1'):
                re += '#'
            else:
                re += ' '
        answer.append(re)
    return answer