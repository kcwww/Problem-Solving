answer = 0

def dfs(numbers, target, result, idx):
    global answer
    if (target == result) and idx == len(numbers):
        answer += 1
        return
    if (idx >= len(numbers)):
        return
    num = [numbers[idx], -numbers[idx]]
    for n in num:
        dfs(numbers, target, result + n, idx + 1)
    return

def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer