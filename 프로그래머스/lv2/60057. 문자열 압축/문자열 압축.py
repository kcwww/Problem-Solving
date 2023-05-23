def solution(s):
    #1개부터 절반까지 문자 잘라서 확인
    #문자 자른뒤 갯수 세기
    # 갯수 만큼 새 문자열 만듬
    answer = []
    print(s)
    length = len(s)
    for i in range(1, length // 2 + 1):
        ss = []
        for c in range(0, length, i):
            ss.append(s[c:c + i])
        stack = []
        cnt = 1
        for w in ss:
            if (len(stack) < 1):
                stack.append(w)
                continue
            word = stack[-1]
            if (w == word):
                cnt += 1
            else:
                if (cnt != 1):
                    stack[-1] = str(cnt) + stack[-1]
                cnt = 1
                stack.append(w)
        if (cnt != 1):
            stack[-1] = str(cnt) + stack[-1]
        stack = ''.join(stack)
        answer.append(len(stack))
    return min(answer) if answer else length