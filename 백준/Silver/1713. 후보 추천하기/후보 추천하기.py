import sys

N = int(sys.stdin.readline().strip())
student = int(sys.stdin.readline().strip())
votes = list(map(int, sys.stdin.readline().split()))

stack = []
photos = {}
for v in votes:
    if v in photos:
        photos[v] += 1
    else:
        photos[v] = 1
    if v in stack:
        continue
    else:
        stack.append(v)
    if len(stack) > N:
        temp = []
        for i in range(N):
            temp.append(photos[stack[i]])
        min_num = min(temp)
        for i in range(N):
            if photos[stack[i]] == min_num:
                photos[stack[i]] = 0
                stack.pop(i)
                break
stack.sort()
print(*stack)
