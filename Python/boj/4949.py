import sys

while True:
	stack = []
	li = list(sys.stdin.readline().rstrip())
	l = len(li)
	flag = 0
	if ( l == 1 and li[0] == '.'):
		break
	for i in li:
		if (i == '('):
			stack.append(i)
		elif (i == '['):
			stack.append(i)
		elif (i == ')'):
			if (len(stack) == 0):
				flag = 1
			elif (stack[-1] != '('):
				flag = 1
			else:
				stack.pop()
		elif (i == ']'):
			if (len(stack) == 0):
				flag = 1
			elif (stack[-1] != '['):
				flag = 1
			else:
				stack.pop()
		if (flag == 1):
			break
	if (flag == 0 and len(stack) == 0):
		print('yes')
	else:
		print('no')
