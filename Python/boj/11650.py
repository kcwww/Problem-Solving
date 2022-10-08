a = int(input())
ans = []


while a:
    b, c = map(int, input().split())
    ans.append([b,c])
    a = a - 1

ans = sorted(ans)

for list in ans:
    x = list[0]
    y = list[1]
    print(x, y)