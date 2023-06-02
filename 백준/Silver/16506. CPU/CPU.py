import sys

opcode = {"ADD" : "0000", "SUB" : "0001","MOV" : "0010", "AND" : "0011",
          "OR" : "0100", "NOT" : "0101", "MULT" : "0110", "LSFTL" : "0111", "LSFTR" : "1000",
          "ASFTR" : "1001", "RL" : "1010", "RR" : "1011"}

TC = int(sys.stdin.readline().strip())
for i in range(TC):
    op, rD, rA, rB_C = sys.stdin.readline().split()
    rD, rA, rB_C = map(int, [rD, rA, rB_C])
    if op[-1] == 'C':
        print(opcode[op[0:-1]] + '1', end="")
    else:
        print(opcode[op] + '0', end="")
    print('0', end="")
    rD = str(bin(rD)[2:])
    while len(rD) != 3:
        rD = '0' + rD
    print(rD, end="")
    rA = str(bin(rA)[2:])
    while len(rA) != 3:
        rA = '0' + rA
    print(rA, end="")
    rB_C = str(bin(rB_C)[2:])
    if op[-1] == 'C':
        while len(rB_C) != 4:
            rB_C = '0' + rB_C
    else:
        while len(rB_C) != 3:
            rB_C = '0' + rB_C
        rB_C += '0'
    print(rB_C)

