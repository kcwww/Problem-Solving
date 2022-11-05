import sys
from collections import deque

num, tc = map(int, sys.stdin.readline().split())
de = deque(range(1,num+1))
cnt = 1
li = []
while len(de) != 0:
    if (cnt == tc):
        n = de.popleft()
        cnt = 1
        li.append(n)
    else:
        n = de.popleft()
        de.append(n)
        cnt += 1

for i in li:
    if (i == li[0]):
        print("<",end="")
    if (i == li[-1]):
        print(i,">", sep="")
    else:
        print(i, end= ", ")