def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x : [x[col - 1], -x[0]])
    
    idx = row_begin
    for num in data[row_begin - 1: row_end]:
        sum_mod = 0
        for n in num:
            sum_mod += n % idx
        idx += 1
        answer ^= sum_mod
    return answer