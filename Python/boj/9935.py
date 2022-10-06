a = input().strip()
b = input().strip()
n = len(b)
stack=[]
b_list = list(b)
for char in a:
    stack.append(char)
    if stack[-n:] == b_list:
        del stack[-n:]
if stack == []:
  print('FRULA')
else:
  print(''.join(stack))
