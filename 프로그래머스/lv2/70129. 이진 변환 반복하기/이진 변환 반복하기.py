def solution(s):
    answer = []
    zeros = 0
    idx = 0
    while (s != '1'):
        zeros += s.count('0')
        s = s.replace('0','')
        num = len(s)
        binary = bin(num)
        binary = binary[2:]
        s = binary
        idx += 1
    answer.append(idx)
    answer.append(zeros)
    return answer