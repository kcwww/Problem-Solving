def solution(number, k):
    stack = []
    for i in number:
        if len(stack) == 0:
            stack.append(i)
            continue
        while len(stack) > 0 and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
    while k > 0:
        k -= 1
        stack.pop()
    return ''.join(stack)