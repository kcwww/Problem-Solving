import sys

def shine(dir, box, nums, i, j):
    move = [[0,1],[-1, 0],[0, -1], [1, 0]]
    row, col = len(box), len(box[0])
    r, c = i, j
    while True:
        if box[r][c] == 1:
            dir += 1
            if dir == 2 or dir == 4:
                dir -= 2
        r = r + move[dir][0]
        c = c + move[dir][1]
        if r >= 0 and r < row and c >= 0 and c < col:
            continue
        else:
            return nums[r + 1][c + 1]
    return 0


row, col = map(int, sys.stdin.readline().split())

box = []
nums = []
for _ in range(row):
    mirror = list(map(int, sys.stdin.readline().split()))
    box.append(mirror)
    nums.append([0] * (col + 2))

for _ in range(2):
    nums.append([0] * (col + 2))

num = 1
for i in range(1, row + 1):
    nums[i][0] = num
    num += 1
for i in range(1, col + 1):
    nums[row + 1][i] = num
    num += 1
for i in range(row, 0, -1):
    nums[i][col + 1] = num
    num += 1
for i in range(col, 0, -1):
    nums[0][i] = num
    num += 1

result = []


for i in range(row):
    out = shine(0, box, nums, i, 0)
    result.append(out)
for j in range(col):
    out = shine(1, box, nums, row - 1, j)
    result.append(out)
for i in range(row - 1, -1, -1):
    out = shine(2, box, nums, i, col - 1)
    result.append(out)
for j in range(col - 1, -1, -1):
    out = shine(3, box, nums, 0, j)
    result.append(out)

print(*result)
