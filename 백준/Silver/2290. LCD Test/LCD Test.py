import sys

s, numbers = sys.stdin.readline().split()
s = int(s)
col = s + 2
row = s * 2 + 3

for i in range(row):
    for num in numbers:
        if i == 0 or i == row - 1:
            if num == '7' and i == row - 1:
                print(' ' * col, end=' ')
            elif num == '1' or num == '4':
                print(' ' * col, end=' ')
            else:
                print(' ' + '-' * s +' ', end=' ')
        elif i < (row // 2):
            if num == '5' or num == '6': #1237 4890 56
                print('|' + ' ' * (col - 1), end=" ")
            elif num == '1' or num == '2' or num == '3' or num == '7':
                print(' ' * (col - 1) + '|', end=" ")
            else:
                print('|' + ' ' * (col - 2) + '|', end=" ")
        elif i == row // 2:
            if num == '1' or num == '7' or num == '0':
                print(' ' * col, end=" ")
            else:
                print(' ' + (col - 2) * '-' + ' ', end=" ")
        else:
            if num == '2':
                print('|' + ' ' * (col - 1), end=" ")
            elif num == '0' or num == '6' or num == '8':
                print('|' + ' '* (col - 2) + '|', end=" ")
            else:
                print(' ' * (col - 1) + '|', end=" ")
    print()