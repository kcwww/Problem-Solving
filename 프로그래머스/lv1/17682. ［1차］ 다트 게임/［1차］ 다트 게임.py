import math

def solution(dartResult):
    dart = []
    size = len(dartResult)
    parse = []
    for i in range(size):
        if (ord(dartResult[i]) >= ord('0') and ord(dartResult[i]) <= ord('9') and \
            i != 0 and dartResult[i - 1] != '1'):
            dart.append(parse)
            parse = []
        parse.append(dartResult[i])
    dart.append(parse)
    
    idx = 0
    answer = []
    for da in dart:
        str_num = ''
        for d in da:
            if (ord(d) >= ord('0') and ord(d) <= ord('9')):
                str_num += d
            if (d == 'S'):
                answer.append(int(str_num))
            elif (d == 'D'):
                answer.append(math.pow(int(str_num), 2))
            elif (d == 'T'):
                answer.append(math.pow(int(str_num), 3))
                
            if (d == '#'):
                answer[idx] *= -1
            elif (d == '*'):
                answer[idx] *= 2
                if (idx > 0):
                    answer[idx - 1] *= 2
        idx += 1
    return sum(answer)