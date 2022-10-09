import sys

num = int(sys.stdin.readline().strip())
li = []
while num:
	li.append(int(sys.stdin.readline().strip()))
	num = num - 1
li = sorted(li)
for i in li:
	print(i)
