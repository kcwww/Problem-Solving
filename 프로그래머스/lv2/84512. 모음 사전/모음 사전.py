flag = 0
result = 0

def dfs(compare, alpha, word):
    global flag, result
    if (compare == word):
        flag = 1
        return
    result += 1
    if len(compare) >= 5:
        return
    
    for i in range(5):
        if (flag == 1):
            return
        compare.append(alpha[i])
        dfs(compare, alpha, word)
        compare.pop()

def solution(word):
    global result
    alpha = ['A','E','I','O','U']
    word = list(word)
    dfs([], alpha, word)
    return result