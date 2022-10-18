import sys

tc = int(sys.stdin.readline().strip())

while tc:
    paren = list(sys.stdin.readline().strip())
    re = []
    flag = 0
    for i in paren:
        if (i == '('):
            re.append('(')
        else:
            if (len(re) == 0):
                flag = 1
                break
            elif (re[-1] != '('):
                flag = 1
                break
            else:
                re.pop()
    if (flag == 0 and len(re) == 0):
        print('YES')
    else:
        print('NO')        
    tc = tc - 1
