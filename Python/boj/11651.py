import sys

tc = int(sys.stdin.readline().rstrip())
ans = []

while tc:
    x,y = list(map(int, sys.stdin.readline().split()))
    ans.append([y,x])
    tc = tc - 1
ans = sorted(ans)
for i in ans:
    print(i[1],i[0])
