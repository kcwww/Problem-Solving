import sys

M = int(sys.stdin.readline().strip())
dasom = int(sys.stdin.readline().strip())
other = []
for _ in range(1, M):
    other.append(int(sys.stdin.readline().strip()))

other.sort(reverse=True)
answer = 0
while other and dasom <= other[0]:
    dasom += 1
    other[0] -= 1
    other.sort(reverse=True)
    answer += 1
print(answer)

