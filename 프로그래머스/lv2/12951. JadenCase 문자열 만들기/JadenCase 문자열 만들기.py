def solution(s):
    answer = ''
    s = s.lower()
    flag = 1
    for c in s:
        if c == ' ':
            flag = 1
        elif flag == 1:
            if c.isalpha():
                c = c.upper()
            flag = 0
        answer += c
    return answer