def solution(s):
    answer = 0
    str_len = len(s)
    same = 0
    diff = 0
    char = s[0]
    for i in range(str_len):
        if (char == s[i]):
            same += 1
        else:
            diff += 1
        if (same == diff):
            answer += 1
            same = 0
            diff = 0
            if (i < (str_len - 1)):
                char = s[i + 1]
    if (same != 0 or diff != 0):
        answer += 1
    return answer