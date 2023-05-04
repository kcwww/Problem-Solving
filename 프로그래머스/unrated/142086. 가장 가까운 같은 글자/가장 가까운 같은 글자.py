def solution(s):
    str_len = len(s)
    answer = []
    for i in range(str_len):
        result = -1
        for j in range(i):
            if s[i] == s[j]:
                result = i - j
        answer.append(result)

    return answer