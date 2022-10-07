import sys
def input():
	return sys.stdin.readline().rstrip()

num = int(input())
stack = []

while num:
	cal = input().split()		
	if (cal[0] == 'push'):
		stack.append(int(cal[1]))
	if (cal[0] == 'pop'):
		if (len(stack) != 0):
			print(stack[-1])
			del(stack[-1])
		else:
			print(-1)
	if (cal[0] == 'size'):
		print(len(stack))
	if (cal[0] == 'empty'):
		if (len(stack) == 0):
			print(1)
		else:
			print(0)
	if (cal[0] == 'top'):
		if (len(stack) == 0):
			print(-1)
		else:
			print(stack[-1])
	num = num - 1
