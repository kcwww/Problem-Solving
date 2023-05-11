def solution(strings, n):
    for i, s in enumerate(strings):
        strings[i] = s[n] + s
    strings.sort()
    return list(x[1::] for x in strings)