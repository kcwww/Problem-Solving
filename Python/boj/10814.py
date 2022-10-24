import sys

tc = int(sys.stdin.readline().rstrip())
ans = []
while tc:
    a,b = sys.stdin.readline().split()
    ans.append([int(a),b])
    tc = tc - 1
ans.sort(key=lambda x : x[0])
for i in ans:
    print(i[0],i[1])
