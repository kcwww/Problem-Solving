from collections import deque

n = int(input())
queue = deque()

for i in range(1,n+1):
    queue.append(i)
d_len = len(queue)

while d_len != 1:
    queue.popleft()
    queue.append(queue.popleft())
    d_len = len(queue)
print(queue[0])