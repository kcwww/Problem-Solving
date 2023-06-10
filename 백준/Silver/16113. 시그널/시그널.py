import sys

numbers = {'0' : ["###","#.#","#.#","#.#","###"], '2' : ["###","..#","###","#..","###"], '3' : ["###","..#","###","..#","###"],
           '4' : ["#.#","#.#","###","..#","..#"], '5' : ["###","#..","###","..#","###"], '6' : ["###","#..","###","#.#","###"], 
           '7' : ["###","..#","..#","..#","..#"], '8' : ["###","#.#","###","#.#","###"], '9' : ["###","#.#","###","..#","###"]}


def check_one(sig, idx, sli):
    for i in range(5):
        if sig[i][idx] != '#':
            return False
    if idx == sli - 1:
        return True
    if sig[0][idx + 1] == '#':
        return False
    return True


lines = int(sys.stdin.readline().strip())
signals = sys.stdin.readline().strip()

sli = lines // 5
sliced_sig = []
for i in range(0, lines, sli):
    sliced_sig.append(signals[i : i + sli])

result = ''
idx = 0
while idx < sli:
    if sliced_sig[0][idx] == '#':
        if check_one(sliced_sig, idx, sli):
            result += '1'
            idx += 1
        else:
            sig_num = []
            for i in range(5):
                sig_num.append(sliced_sig[i][idx: idx + 3])
            for num in numbers:
                if numbers[num] == sig_num:
                    result += num
                    break
            idx += 3
    else:
        idx += 1
print(result)