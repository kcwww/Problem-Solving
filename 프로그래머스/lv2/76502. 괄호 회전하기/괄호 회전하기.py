from collections import deque

def solution(s):
    answer = 0
    de = deque(s)
    for i in range(len(de)):
        new_de = de.copy()
        stack = []
        for p in new_de:
            stack.append(p)
            length = len(stack)
            if stack[-1] == ')':
                if length > 1 and stack[-2] == '(':
                    stack.pop()
                    stack.pop()
            elif stack[-1] == '}':
                if length > 1 and stack[-2] == '{':
                    stack.pop()
                    stack.pop()
            elif stack[-1] == ']':
                if length > 1 and stack[-2] == '[':
                    stack.pop()
                    stack.pop()
        if len(stack) == 0:
            answer += 1
        de.rotate(-1)
    return answer