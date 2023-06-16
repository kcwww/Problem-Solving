import sys

def check_trash(truck, w, l):
    now = truck[2]
    truck[2] = l[0]
    truck[0] = truck[0] + l[0] - now
    truck[1] = truck[1] + l[1]
    if truck[1] == w:
        truck[1] = 0
        truck[0] = truck[0] + truck[2]
        truck[2] = 0
    elif truck[1] > w:
        truck[1] = l[1]
        truck[0] = truck[0] + truck[2] + l[0]
    return

TC = int(sys.stdin.readline().strip())
for _ in range(TC):
    weight, N = map(int, sys.stdin.readline().split())
    location = []
    for i in range(N):
        d, w = map(int, sys.stdin.readline().split())
        location.append([d, w])
    truck = [0, 0, 0]
    for l in location:
        check_trash(truck, weight, l)
    if truck[2] != 0:
        truck[0] += truck[2]
    print(truck[0])
