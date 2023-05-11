def solution(arr):
    answer = []
    for i, n in enumerate(arr):
        if (i > 0):
            if (n == arr[i - 1]):
                continue
            else:
                answer.append(n)
        else:
            answer.append(n)
    return answer