import sys

tc = int(sys.stdin.readline().strip())
count = 0
stack = []
ans = []
flag = 0
while tc:
    num = int(sys.stdin.readline().strip())
    while count < num:
        count += 1
        stack.append(count)
        ans.append('+')
    if (stack[-1] == num):
        stack.pop()
        ans.append('-')
    else:
        flag = 1
    tc = tc - 1
if (flag == 0):
    for i in ans:
        print(i)
else:
    print('NO')
