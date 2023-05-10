def solution(arr1, arr2):
    answer = []
    for i, n in enumerate(arr1):
        result = []
        for m,p in enumerate(n):
            result.append(arr1[i][m] + arr2[i][m])
        answer.append(result)
    return answer