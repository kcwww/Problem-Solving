def solution(n):
    answer = 0
    bin_n = str(bin(n))[2:]
    answer = bin_n.count('1')
    while True:
        n += 1
        re_n = str(bin(n))[2:].count('1')
        if (re_n == answer):
            return n
    return answer