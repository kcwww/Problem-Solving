import sys

line = sys.stdin.readline().strip()
bomb = list(sys.stdin.readline().strip())
stack = []
bomb_size = len(bomb)

for i in line:
    stack.append(i)
    if stack[-1] == bomb[-1]:
         if stack[-bomb_size ::] == bomb:
              del stack[-bomb_size:]
if stack != []:
     print(''.join(stack))
else:
     print('FRULA')
