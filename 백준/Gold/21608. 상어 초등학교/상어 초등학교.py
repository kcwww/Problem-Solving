import sys

def check_empty(N, classroom, i, j, v):
	near = [[-1,0], [0,-1], [0, 1], [1,0]]
	empty = 0
	favor = 0
	for n in near:
		r = i + n[0]
		c = j + n[1]
		if r >= 0 and r < N and c >= 0 and c < N:
			if classroom[r][c] == 0:
				empty += 1
			elif classroom[r][c] in v:
				favor += 1
	return [favor, empty, i, j]


def check_favor(k, v, N, classroom):
	blank = []
	for i in range(N):
		for j in range(N):
			if classroom[i][j] == 0:
				seat = check_empty(N, classroom, i, j, v)
				blank.append(seat)
	blank.sort(key=lambda x : (-x[0], -x[1]))
	classroom[blank[0][2]][blank[0][3]] = k
	return

def check_satisfy(N, classroom, student, i, j):
	satisfy = 0
	near = [[-1,0], [0,-1], [0, 1], [1,0]]
	student_num = classroom[i][j]
	for n in near:
		r = i + n[0]
		c = j + n[1]
		if r >= 0 and r < N and c >= 0 and c < N:
			if classroom[r][c] in student[student_num]:
				satisfy += 1
	if satisfy == 2:
		satisfy = 10
	elif satisfy == 3:
		satisfy = 100
	elif satisfy == 4:
		satisfy = 1000
	return satisfy

N = int(sys.stdin.readline().strip())
student = {}
for i in range(N**2):
	line = list(map(int, sys.stdin.readline().split()))
	student[line[0]] = line[1::]

classroom = []
for _ in range(N):
	classroom.append([0] * N)

for k, v in student.items():
	check_favor(k, v, N, classroom)

satisfy = 0
for i in range(N):
	for j in range(N):
		satisfy += check_satisfy(N, classroom, student, i, j)
print(satisfy)
