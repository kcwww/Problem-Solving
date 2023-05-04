def solution(s, skip, index):
    alpha = {}
    answer = ''
    for c in s:
        char = ord(c)
        for i in range(index):
            char += 1
            if (char > ord('z')):
                char = char - ord('z') + ord('a') - 1
            while (chr(char) in skip):
                char += 1
                if (char > ord('z')):
                    char = char - ord('z') + ord('a') - 1
            
        answer += chr(char)
        
    return answer