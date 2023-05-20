def changeArr(arr, line, querie):
    row = querie[0] - 1
    col = querie[1] - 1
    idx = 0
    for i in range(querie[1], querie[3]):
        arr[row][col] = line[idx]
        idx += 1
        col += 1
    for i in range(querie[0], querie[2]):
        arr[row][col] = line[idx]
        row += 1
        idx += 1
    for i in range(querie[1], querie[3]):
        arr[row][col] = line[idx]
        col -= 1
        idx += 1
    for i in range(querie[0], querie[2]):
        arr[row][col] = line[idx]
        row -= 1
        idx += 1
    return

def makeline(querie, arr, num):
    re = []
    row = querie[0] - 1
    col = querie[1] - 1
    for i in range(querie[1], querie[3]):
        num = arr[row][col]
        re.append(num)
        col += 1
    for i in range(querie[0], querie[2]):
        num = arr[row][col]
        re.append(num)
        row += 1
    for i in range(querie[1], querie[3]):
        num = arr[row][col]
        re.append(num)
        col -= 1
    for i in range(querie[0], querie[2]):
        num = arr[row][col]
        re.append(num)
        row -= 1
    num = re.pop()
    re.insert(0, num)
    return re


def solution(rows, columns, queries):
    #테두리를 하나의 배열로 복사한후
    #바꾼뒤 가장 작은수 넣고 원래 배열에 대입
    answer = []
    arr = []
    num = 1
    col = columns
    for i in range(rows):
        arr.append(list(range(num, col + 1)))
        num += columns
        col += columns
    for q in queries:
        line = makeline(q, arr, columns)
        answer.append(min(line))
        changeArr(arr, line, q)
    return answer