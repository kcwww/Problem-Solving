def solution(A,B):
    # A의 최소 * B 의 최대
    # A의 다음 최소 * B의 다음 최대 반복 -> 시간초과..
    # A 를 내림차순 정렬 B 를 오름차순 정렬
    answer = 0
    A.sort(reverse=True)
    B.sort()
    while A:
        mini = A.pop()
        maxi = B.pop()
        answer += mini * maxi
    return answer