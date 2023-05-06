def solution(sizes):
    max_num = 0
    min_num = 0
    number = len(sizes)
    for i in range(number):
        sizes[i] = sorted(sizes[i])
    
    for i in range(number):
        if (max_num < sizes[i][1]):
            max_num = sizes[i][1]
        if (min_num < sizes[i][0]):
            min_num = sizes[i][0]
    
    return max_num * min_num