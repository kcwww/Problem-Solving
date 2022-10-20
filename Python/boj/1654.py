import sys

lan_line, need_line = map(int, sys.stdin.readline().split())
line_li = []

while lan_line:
    line_li.append(int(sys.stdin.readline().rstrip()))
    lan_line = lan_line - 1

start = 1
end = max(line_li)

while start <= end:
    mid = (start + end) // 2
    l = 0
    for i in line_li:
        l += (i // mid)
    if (l >= need_line):
        start = mid + 1
    else:
        end = mid - 1
print(end)
