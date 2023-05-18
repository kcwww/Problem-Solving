def dfs(i, wires, visited):
    global cnt
    if (visited[i] == 1):
        return
    visited[i] = 1
    one = wires[i][0]
    two = wires[i][1]
    for j, w in enumerate(wires):

        if one in w:
            dfs(j, wires, visited)
        if two in w:
            dfs(j, wires, visited)
    
    

def solution(n, wires):
    answer = []
    visited = [0] * n
    for cut in range(len(wires)):
        visited[cut] = 1
        num = []
        for i, w in enumerate(wires):
            if (visited[i] == 1):
                continue
            dfs(i, wires, visited)
            num.append(visited.count(1))

        if (len(num) == 1):
            answer.append([1, num[0]])
        else:
            answer.append([num[0], n - num[0]])
        visited = [0] * n

    return min(abs(x[0] - x[1]) for x in answer)