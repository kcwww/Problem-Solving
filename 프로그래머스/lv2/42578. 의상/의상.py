def solution(clothes):
    clo = {}
    for c in clothes:
        if c[1] in clo:
            clo[c[1]] += 1
        else:
            clo[c[1]] = 1
    mul = 1
    for v in clo.values():
        mul *= (v + 1)
    return mul - 1