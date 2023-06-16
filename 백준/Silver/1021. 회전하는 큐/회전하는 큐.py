from collections import deque
import sys

size, N = map(int, sys.stdin.readline().split())

deq = deque(list(range(1,size + 1)))
want = list(map(int, sys.stdin.readline().split()))

answer = 0
for w in want:
    idx = deq.index(w)
    if idx > (size // 2):
        while deq[0] != w:
            num = deq.pop()
            deq.appendleft(num)
            answer += 1
    else:
        while deq[0] != w:
            num = deq.popleft()
            deq.append(num)
            answer += 1
    deq.popleft()
    size -= 1
print(answer)
