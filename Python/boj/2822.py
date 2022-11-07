import sys

score = []
for i in range(8):
    score.append(int(sys.stdin.readline().rstrip()))
ans = sorted(score)

sum_num = sum(ans[3:]) 
print(sum_num)
num_li = []

for i in ans[3:]:
    for j in range(8):
        if (i == score[j]):
            num_li.append(j + 1)
num_li = sorted(num_li)
for i in num_li:
    print(i,end=" ")
