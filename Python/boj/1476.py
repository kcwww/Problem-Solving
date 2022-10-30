import sys

E, S, M = map(int, sys.stdin.readline().split())

cnt = 0

Ei = 0
Si = 0
Mi = 0

while True:
    if (E == Ei and S == Si and M == Mi):
        break
    cnt += 1
    Ei += 1
    Si += 1
    Mi += 1
    if (Ei > 15):
        Ei = 1
    if (Si > 28):
        Si = 1
    if (Mi > 19):
        Mi = 1
print(cnt)
