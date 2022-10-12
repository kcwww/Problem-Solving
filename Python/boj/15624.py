import sys

n = int(sys.stdin.readline().strip())

a, b = 0, 1
temp = a + b

for i in range(n):
    a = b % 1000000007
    b = temp % 1000000007
    temp = a + b    
print(a)
