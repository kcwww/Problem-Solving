from collections import deque
def solution(s):
    stack = deque()
    for c in s:
        if c == ')':
            if not stack:
                return False
            compare = stack.pop()
            if compare == ')':
                return False
        else:
            stack.append(c)
        

    return False if stack else True