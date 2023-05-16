def solution(k, ranges):
    answer = []
    height = []
    while k != 1:
        height.append(k)
        if (k % 2) == 0:
            k //= 2
        else:
            k = k * 3 + 1
    height.append(1)
    size = len(height)
    
    for i in range(0, size - 1):
        answer.append((height[i] + height[i + 1]) / 2)
    
    result = []
    for i in ranges:
        if i[0] >= (size + i[1]):
            result.append(-1.0)
        else:
            result.append(sum(answer[i[0]:size + i[1] - 1]))
    return result