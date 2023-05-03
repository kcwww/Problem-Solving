def key_result(keymap, target):
    re = 0
    
    for char in target:
        
        num = 101
        temp = 102
        for key in keymap:
            if char in key:
                temp = key.index(char) + 1
            if num > temp:
                num = temp
        if (temp == 102):
            return (-1)
        re += num
        
        
    return (re)

def solution(keymap, targets):
    answer = []
    for tarr in targets:
        answer.append(key_result(keymap, tarr))
    
    return answer