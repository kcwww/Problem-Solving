import sys

def move_cloud(cloud, maps, d, s, N):
	# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
	move = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

	for i in range(len(cloud)):
		x, y = cloud[i][0], cloud[i][1]
		for _ in range(s):
			r = x + move[d][0]
			c = y + move[d][1]
			if r >= 0 and r < N and c >= 0 and c < N:
				x, y = r, c
			else:
				if r < 0:
					r = N - 1
				elif r == N:
					r = 0
				if c < 0:
					c = N - 1
				elif c == N:
					c = 0
				x, y = r, c
		cloud[i][0], cloud[i][1] = x, y
	return

def rain_and_check(cloud, maps, N, visited):
	basket = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
	for i in range(len(cloud)):
		x, y = cloud[i][0], cloud[i][1]
		visited[x][y] = 1
		maps[x][y] += 1
	for i in range(len(cloud)):
		x, y = cloud[i][0], cloud[i][1]
		for b in basket:
			r = x + b[0]
			c = y + b[1]
			if r >= 0 and r < N and c >= 0 and c < N:
				if maps[r][c] > 0:
					maps[x][y] += 1
	return

def new_cloud(cloud, maps, N, visited):
	temp = []
	for i in range(N):
		for j in range(N):
			if visited[i][j] == 1:
				visited[i][j] = 0
				continue
			if maps[i][j] >= 2:
				temp.append([i, j])
				maps[i][j] -= 2
	return temp

N, M = map(int, sys.stdin.readline().split())

maps = []
visited = []
for _ in range(N):
	line = list(map(int, sys.stdin.readline().split()))
	maps.append(line)
	visited.append([0] * N)

order = []
for _ in  range(M):
	d, s = map(int, sys.stdin.readline().split())
	order.append([d, s])

cloud = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]


for o in order:
	d, s = o[0], o[1]
	d -= 1
	move_cloud(cloud, maps, d, s, N)
	rain_and_check(cloud, maps, N, visited)
	cloud = new_cloud(cloud, maps, N, visited)

result = 0

for m in maps:
	result += sum(m)
print(result)
