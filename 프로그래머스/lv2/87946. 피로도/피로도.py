from itertools import permutations

def solution(k, dungeons):
    answer = -1
    s = permutations(dungeons, len(dungeons))
    for i in s:
        st = k
        cnt = 0
        for dungeon in i:
            if (st >= dungeon[0]):
                st -= dungeon[1]
                cnt += 1
        if (cnt > answer):
            answer = cnt
    return answer