def solution(t, p):
    str_len = len(t)
    slice_len = len(p)
    num = int(p)
    answer = 0
    for i in range(str_len):
        if (i + slice_len - 1) < str_len:
                
            if (num >= int(t[i: i+slice_len])):
                answer += 1
    return answer