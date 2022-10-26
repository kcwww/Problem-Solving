import sys

tc = int(sys.stdin.readline().rstrip())
num_li = list(map(int,sys.stdin.readline().split()))
num_li = sorted(num_li)

ftc = int(sys.stdin.readline().rstrip())
f_li = list(map(int,sys.stdin.readline().split()))

i = 0
while i < ftc:
    start = 0
    end = tc - 1
    flag = 0
    while start <= end:
        mid = (start + end) // 2
        if (f_li[i] > num_li[mid]):
            start = mid + 1
        elif (f_li[i] == num_li[mid]):
            flag = 1
            print(flag)
            break
        else:
            end = mid - 1
    if (flag == 0):
        print(0)
    i += 1
