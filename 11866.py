import sys
from collections import deque

num, c = map(int,sys.stdin.readline().split())
de = deque(range(1,num + 1))
ans = []

s = 0
while True:
    if (len(de) == 0):
        break
    if (s != c - 1):
        n = de.popleft()
        de.append(n)
        s += 1
    else:
        n = de.popleft()
        ans.append(n)
        s = 0
print("<", end="")
for i in ans:
    print(i,end="")
    if (i != ans[-1]):
        print(", ", end="")
print(">")
