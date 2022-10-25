import sys

tc = int(sys.stdin.readline().rstrip())
li = []
while tc:
    li.append(sys.stdin.readline().rstrip())
    tc = tc - 1

li = set(li)
li = sorted(li)
li = sorted(li,key = len)
for i in li:
    print(i)
