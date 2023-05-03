def solution(wallpaper):
    wallpaper = [list(row) for row in wallpaper]
    u = len(wallpaper)
    d = 0
    l = len(wallpaper[0])
    r = 0
    row = u
    col = l
    for i in range(row):
        for j in range(col):
            if (wallpaper[i][j] == '#'):

                if (u > i):
                    u = i
                if (d < i):
                    d = i
                if (l > j):
                    l = j
                if (r < j):
                    r = j
    answer = [u,l, d+1,r+1]
    return answer