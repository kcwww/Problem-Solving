import sys
from collections import deque

tc = int(sys.stdin.readline().rstrip())
de = deque()
while tc:
	in_put = sys.stdin.readline().rstrip()
	if (in_put[:4] == "push"):
		num = int(in_put[5:])
		de.append(num)
	elif (in_put == "front"):
		if (len(de) == 0):
			print(-1)
		else:
			print(de[0])
	elif (in_put == "back"):
		if (len(de) == 0):
			print(-1)
		else:
			print(de[-1])
	elif (in_put == "pop"):
		if (len(de) == 0):
			print(-1)
		else:
			num = de.popleft()
			print(num)
	elif (in_put == "size"):
		print(len(de))
	elif (in_put == "empty"):
		if (len(de) == 0):
			print(1)
		else:
			print(0)
	tc = tc - 1
