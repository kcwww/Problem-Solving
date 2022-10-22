import sys

tree, wood = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(trees)

while start <= end:
	wood_sum = 0
	mid = (start + end) // 2
	for i in trees:
		if (i > mid):
			wood_sum += i - mid
	if (wood > wood_sum):
		end = mid - 1
	else:
		start = mid + 1
print(end)
