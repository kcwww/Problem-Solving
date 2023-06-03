def solution(n, t, m, p):
    # 총 n * t 만큼 리스트를 만들어야함
    answer = ''
    size = m * t
    stack = ['0']
    for i in range(1, size + 1):
        number = ''
        while i > 0:
            num = i % n
            if (num > 9):
                num = num - 10 + ord('A')
                num = chr(num)
            else:
                num = str(num)
            i //= n
            number = num + number
        stack += list(number)
    for i in range(t):
        answer += stack[(i * m) + p - 1]
    return answer