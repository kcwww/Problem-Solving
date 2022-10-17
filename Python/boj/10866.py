import sys
from collections import deque

tc = int(sys.stdin.readline().strip())
de = deque()

while tc:
    input_de = sys.stdin.readline().strip()
    if (input_de[0:9] == "push_back"):
        de.append(input_de[10:])
    elif (input_de[0:10] == "push_front"):
        de.appendleft(input_de[11:])
    elif (input_de == "front"):
        if (len(de) == 0):
            print(-1)
        else:
            print(de[0])
    elif (input_de == "back"):
        if (len(de) == 0):
            print(-1)
        else:
            print(de[-1])
    elif (input_de == "empty"):
        if (len(de) == 0):
            print(1)
        else:
            print(0)
    elif (input_de == "size"):
        print(len(de))
    elif (input_de == "pop_front"):
        if (len(de) == 0):
            print(-1)
        else:
            num = de.popleft()
            print(num)
    elif (input_de == "pop_back"):
        if (len(de) == 0):
            print(-1)
        else:
            num = de.pop()
            print(num)
    tc = tc - 1
