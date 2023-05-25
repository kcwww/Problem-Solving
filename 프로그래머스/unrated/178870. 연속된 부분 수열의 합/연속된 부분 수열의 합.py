def solution(sequence, k):
    #num 스택으로 쌓아서 위치찾기
    answer = []
    start = 0
    nums = 0
    for i, n in enumerate(sequence):
        while (nums + n) > k:
            nums -= sequence[start]
            start += 1
        nums = nums + n
        if nums == k:
            if len(answer) > 0 and (answer[1] - answer[0]) <= (i - start):
                continue
            answer = [start, i]
    return answer