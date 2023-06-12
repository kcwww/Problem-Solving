import sys

N, M = map(int, sys.stdin.readline().split())

set_N = {}
for _ in range(N):
    string = sys.stdin.readline().strip()
    set_N[string] = 1

answer = 0
for _ in range(M):
    string = sys.stdin.readline().strip()
    if string in set_N:
        answer += 1
print(answer)
