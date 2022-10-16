import sys
from collections import deque

tc = int(sys.stdin.readline().strip())
stack = deque()
while tc:
	num = int(sys.stdin.readline().strip())
	if (num == 0):
		if (len(stack) == 0):
			pass
		else:
			stack.pop()
	else:
		stack.append(num)
	tc = tc - 1
print(sum(stack))
