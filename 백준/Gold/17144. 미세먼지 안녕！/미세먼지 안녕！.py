import sys
from collections import deque

# 먼지가 5 이상인 부분 체크
# 체크한 부분 동시에 확산 진행
# 공기청정지 위치 기준으로 바람 이동

def sum_dust(R, maps):
	result = 0
	for i in range(R):
		result += sum(maps[i])
	return result + 2

def check_dust(R, C, maps, dust):
	for i in range(R):
		for j in range(C):
			if maps[i][j] >= 5:
				dust[i][j] = maps[i][j]
	return

def diffusion_dust(R, C, maps, dust):
	move = [[1,0], [-1,0], [0,1], [0,-1]]
	for i in range(R):
		for j in range(C):
			if dust[i][j] >= 5:
				num = dust[i][j] // 5
				for m in move:
					x = i + m[0]
					y = j + m[1]
					if x >= 0 and x < R and y >= 0 and y < C and maps[x][y] != -1:
						maps[x][y] += num
						maps[i][j] -= num
				dust[i][j] = 0
	return

def move_wind(R, C, maps):
	air = 0
	for i in range(R):
		if maps[i][0] == -1:
			air = i
			break
	top = deque()
	bottom = deque()
	for j in range(1, C - 1):
		top.append(maps[air][j])
		bottom.append(maps[air + 1][j])
	for i in range(air, 0, -1):
		top.append(maps[i][C - 1])
	for i in range(air + 1, R - 1):
		bottom.append(maps[i][C - 1])
	for j in range(C - 1, 0, -1):
		top.append(maps[0][j])
		bottom.append(maps[R - 1][j])
	for i in range(0, air):
		top.append(maps[i][0])
	for i in range(R - 1, air + 1, -1):
		bottom.append(maps[i][0])

	top.appendleft(0)
	bottom.appendleft(0)
	top.pop()
	bottom.pop()
	idx = 0
	for j in range(1, C - 1):
		maps[air][j] = top[idx]
		maps[air + 1][j] = bottom[idx]
		idx += 1
	b_idx = idx
	for i in range(air, 0, -1):
		maps[i][C - 1] = top[idx]
		idx += 1
	for i in range(air + 1, R - 1):
		maps[i][C - 1] = bottom[b_idx]
		b_idx += 1
	for j in range(C - 1, 0, -1):
		maps[0][j] = top[idx]
		maps[R - 1][j] = bottom[b_idx]
		idx += 1
		b_idx += 1
	for i in range(0, air):
		maps[i][0] = top[idx]
		idx += 1
	for i in range(R - 1, air + 1, -1):
		maps[i][0] = bottom[b_idx]
		b_idx += 1
	return

#####################################################

R, C, T = map(int, sys.stdin.readline().split())


maps = [0] * R
dust = [0] * R
for i in range(R):
	dust[i] = [0] * C
	maps[i] = list(map(int, sys.stdin.readline().split()))

while T > 0:
	check_dust(R,C, maps, dust)
	diffusion_dust(R, C, maps, dust)
	move_wind(R, C, maps)
	T -= 1
print(sum_dust(R, maps))

