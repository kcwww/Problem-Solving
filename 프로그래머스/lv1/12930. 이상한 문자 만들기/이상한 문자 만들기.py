def solution(s):
    st = ''
    idx = 0
    for c in s:
        if (c == ' '):
            idx = 0
            st += ' '
            continue
        if (idx % 2) == 0:
            st += c.upper()
        else:
            st += c.lower()
        idx += 1
        
            
    return st