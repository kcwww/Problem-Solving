def solution(s, n):
    s = list(s)
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
        else:
            alpha = ord(c) + n
            if (alpha > ord('z') and ord(c) >= ord('a') and ord(c) <= ord('z')):
                answer += chr(alpha - ord('z') + ord('a') - 1)
            elif (alpha > ord('Z') and ord(c) >= ord('A') and ord(c) <= ord('Z')):
                answer += chr(alpha - ord('Z') + ord('A') - 1)
            else:
                answer += chr(alpha)
    return answer