import sys

str = list(sys.stdin.readline().split())

for i in range(1, len(str)):
    data_type = str[0]
    data = list(str[i])
    if data[-1] == ',' or data[-1] == ';':
        data.pop()
    while data:
        tmp = data.pop()
        if tmp == '*' or tmp == '&':
            data_type += tmp
        elif tmp == ']':
            data.pop()
            data_type += '[]'
        else:
            data.append(tmp)
            break
    data = ''.join(data) + ';'
    print(data_type, data)
