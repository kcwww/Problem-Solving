def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    st = ''
    for s in n:
        st += s
    return int(st)