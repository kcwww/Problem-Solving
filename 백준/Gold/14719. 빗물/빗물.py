import sys

height , width = map(int, sys.stdin.readline().split())

blocks = list(map(int, sys.stdin.readline().split()))

rain = 0
stack = []
base = 0
for b in blocks:
    stack.append(b)
    if len(stack) > 1 and stack[base] < b:
        for i in range(base, len(stack)):
            if stack[base] > stack[i]:
                rain += (stack[base] - stack[i])
                stack[i] = stack[base]
        base = len(stack) - 1
    elif len(stack) > 1:
        for i in range(base, len(stack)):
            if b > stack[i]:
                rain += (b - stack[i])
                stack[i] = b

print(rain)
