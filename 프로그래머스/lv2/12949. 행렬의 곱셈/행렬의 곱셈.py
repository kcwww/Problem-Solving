def solution(arr1, arr2):
    answer = []
    size = len(arr1[0])
    size2 = len(arr2[0])
    for a in arr1:
        nums = []
        for j in range(size2):
            num = 0
            for i in range(size):
                num += a[i] * arr2[i][j]
            nums.append(num)
        answer.append(nums)
    return answer