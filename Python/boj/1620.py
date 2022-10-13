import sys

N,M = map(int,sys.stdin.readline().split())
pokemon = {}
pokemon_idx = {}
i = 1
while i <= N:
    pokemon[i] = sys.stdin.readline().strip()
    pokemon_idx[pokemon[i]] = i
    i += 1
while M:
	question = sys.stdin.readline().strip()
	if (question[0] >= '0' and question[0] <= '9'):
		print(pokemon[int(question)])
	else:
		print(pokemon_idx[question])
	M = M - 1
