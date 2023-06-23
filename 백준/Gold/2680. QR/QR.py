from sys import stdin
input = stdin.readline

for t in range(int(input())):
    ans = ''
    length = 0
    s = input().strip()

    def convert_binary(_hex):
        _bin = ''
        for i in range(len(_hex)):
            _bin += bin(int(_hex[i], 16))[2:].zfill(4)
        return _bin

    def number(index):
        global ans, length
        count_bit = int(bs[index:index+10], 2)
        index += 10
        while count_bit:
            if count_bit >= 3:
                ans += str(int(bs[index:index+10], 2)).zfill(3)
                count_bit -= 3
                index += 10
                length += 3
            elif count_bit == 2:
                ans += str(int(bs[index:index+7], 2)).zfill(2)
                count_bit -= 2
                index += 7
                length += 2
            elif count_bit == 1:
                ans += str(int(bs[index:index+4], 2))
                count_bit -= 1
                index += 4
                length += 1
        return index

    def alpha(index):
        alphanum = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:')
        global ans, length
        count_bit = int(bs[index:index+9], 2)
        index += 9
        while count_bit:
            if count_bit >= 2:
                temp = int(bs[index:index+11], 2)
                ans += alphanum[temp//45]
                ans += alphanum[temp%45]
                count_bit -= 2
                index += 11
                length += 2
            elif count_bit == 1:
                temp = int(bs[index:index+6], 2)
                ans += alphanum[temp]
                count_bit -= 1
                index += 6
                length += 1
        return index

    def eight(index):
        global ans, length
        count_bit = int(bs[index:index+8], 2)
        index += 8
        for _ in range(count_bit):
            temp = int(bs[index:index+8], 2)
            if temp == 0x20:
                ans += ' '
            elif temp == 0x23:
                ans += '\\#'
            elif temp == 0x5c:
                ans += '\\\\'
            elif 0x20 <= temp <= 0x7e:
                ans += chr(temp)
            else:
                ans += ('\\'+hex(temp)[2:].upper().zfill(2))
            index += 8
            length += 1
        return index

    def kanji(index):
        global ans, length
        count_bit = int(bs[index:index+8], 2)
        index += 8
        for _ in range(count_bit):
            temp = int(bs[index:index+13], 2)
            ans += ('#'+hex(temp)[2:].upper().zfill(4))
            index += 13
            length += 1
        return index

    def solve(_index):
        while _index < len(bs):
            if bs[_index:_index+4] == "0001":
                _index = number(_index+4)
            elif bs[_index:_index+4] == "0010":
                _index = alpha(_index+4)
            elif bs[_index:_index+4] == "0100":
                _index = eight(_index+4)
            elif bs[_index:_index+4] == "1000":
                _index = kanji(_index+4)
            elif bs[_index:_index+4] == "0000":
                return
            else:
                return

    bs = convert_binary(s)
    solve(0)
    print(length, ans)