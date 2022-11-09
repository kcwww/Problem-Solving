import sys

jemi = list(map(int,sys.stdin.readline().split()))
team = list(map(int,sys.stdin.readline().split()))

jemi_sum = 0
team_sum = 0
flag = 0
tlag = 0
for i in range(9):
    jemi_sum += jemi[i]
    if (jemi_sum > team_sum):
        flag = 1
    team_sum += team[i]
    if (flag == 1 and team_sum > jemi_sum):
        print("Yes")
        tlag = 1
        break
if (tlag == 0):
	print("No")
