import sys

def press_switch(switches, idx):
    if switches[idx] == 0:
        switches[idx] = 1
    else:
        switches[idx] = 0
    return

def press_man(switch, switches, num):
    for i in range(switch):
        if (i + 1) % num == 0:
            press_switch(switches, i)
    return

def press_woman(switch, switches, num):
    idx = 1
    i = num - 1
    press_switch(switches, i)
    while i + idx < switch and i - idx >= 0:
        if switches[i + idx] == switches[i - idx]:
            press_switch(switches, i + idx)
            press_switch(switches, i - idx)
            idx += 1
        else:
            break
    return

switch = int(sys.stdin.readline().strip())
switches = list(map(int, sys.stdin.readline().split()))

peoples = int(sys.stdin.readline().strip())

for i in range(peoples):
    gender, num = map(int, sys.stdin.readline().split())
    if gender == 1:
        press_man(switch, switches, num)
    else:
        press_woman(switch, switches, num)

for i in range(1, switch + 1):
    print(switches[i - 1], end=' ')
    if i % 20 == 0:
        print()
