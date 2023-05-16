def solution(elements):
    answer = 0
    size = len(elements)
    setd = set()
    for i in range(1, size + 1):
        for j in range(size):
            if (j + i) > size:
                num = sum(elements[j::])
                num = num + sum(elements[0: j+i-size])
            else:
                num = sum(elements[j : j + i])
            setd.add(num)
    return len(setd)