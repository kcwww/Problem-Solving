import sys

N = int(sys.stdin.readline().strip())

answer = [x % 3 for x in range(N)]
init = list(map(int, sys.stdin.readline().split()))
rule = list(map(int, sys.stdin.readline().split()))

card = [x for x in init]
result = 0
while card != answer:
    new_card = [0] * len(card)
    idx = 0
    for _ in range(len(init)):
        num = card[idx]
        new_idx = rule[idx]
        new_card[new_idx] = num
        idx += 1
    card = new_card
    if new_card == init:
        break
    result += 1
if init == answer:
    print(0)
elif card == init:
    print(-1)
else:
    print(result)
