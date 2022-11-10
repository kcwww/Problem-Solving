import sys

fruit, snake = map(int,sys.stdin.readline().split())
fruit_li = list(map(int,sys.stdin.readline().split()))

flag = 1

while flag == 1:
    flag = 0
    for i in range(fruit):
        if (snake >= fruit_li[i] and fruit_li[i] != 0):
            snake += 1
            fruit_li[i] = 0
            flag = 1
print(snake)
