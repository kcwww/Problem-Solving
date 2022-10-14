import sys
from collections import deque

tc = int(sys.stdin.readline().strip())

def	ft_max(de):
	l = len(de)
	fmax = 0
	for i in range(l):
		if (fmax < de[i]):
			fmax = de[i]
	return (fmax)

while tc:
	card, idx = map(int, sys.stdin.readline().split())
	de = deque(map(int, sys.stdin.readline().split()))
	result = (de[idx])
	max_num = ft_max(de)
	count = 0
	while True:

		ans = 0
		if (de[0] < max_num):
			de.append(de[0])
			de.popleft()
			idx = idx - 1
			if (idx < 0):
				idx = len(de) - 1
		elif (de[0] == max_num):
			ans = de.popleft()
			count += 1
			max_num = ft_max(de)
			idx = idx - 1
		if (result == ans and idx == -1):
			print(count)
			break
	tc = tc - 1
