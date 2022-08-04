import math
import sys
table = {}
dict_sequence = {}
if sys.argv[1] == "-t":
    flag = True
    b = int(sys.argv[2])
    g = int(sys.argv[3])
    max_size = int(sys.argv[4])
    with open(sys.argv[5]) as txt:
        sequence = txt.readlines()
        sequence = [int(i) for i in sequence]
else:
    flag = False
    b = int(sys.argv[1])
    g = int(sys.argv[2])
    max_size = int(sys.argv[3])
    with open(sys.argv[4]) as txt:
        sequence = txt.readlines()
        sequence = [int(i) for i in sequence]

for i in range(len(sequence)-1):
    dict_sequence[sequence[i]] = sequence[i+1]


def DetectCycle(x, f):
    global b
    if flag:
        b = int(sys.argv[2])
    else:
        b = int(sys.argv[1])
    y = x
    i = 0
    m = 0
    while True:
        if i % b == 0 and m == max_size:
            b = 2*b
            Purge(table, b)
            m = math.ceil(m/2)
        if i % b == 0:
            InsertInTable(table, y, i)
            m = m+1
        y = f(y)
        i = i+1
        if i % (g*b) < b:
            j = SearchTableY(table, y)
            if j != -1:
                return (y, i, j)


def InsertInTable(table, y, i):
    table[y] = i


def SearchTableY(table, y):
    min_pos = 900000000000000000
    p = -1
    for i in table:
        if i == y:
            if table[i] < min_pos:
                min_pos = table[i]
                p = min_pos
    return p


def SearchTableJ(table, j):
    p = -1
    for i in table:
        if table[i] == j:
            p = i
            return p
    return p


def f(y):
    return dict_sequence[y]


def Purge(table, b):
    indexes = []
    for i in table:
        if table[i] % b != 0:
            indexes.append(i)
    for i in indexes:
        del table[i]


def Sort_Dict(table):
    table = dict(sorted(table.items()))
    return table


def RecoverCycle(f, y, i, j):
    global b
    c = 1
    found_c = False
    y_c = y
    while c <= (g+1)*b and found_c == False:
        y_c = f(y_c)
        if y == y_c:
            found_c = True
        else:
            c = c+1
    if found_c == False:
        c = i-j
    block_length = g*b
    final_block = block_length*math.floor(i/block_length)
    previous_block = final_block-block_length
    i1 = max(c, previous_block)
    j1 = i1-c
    l = j1+1
    index1 = SearchTableJ(table, b*(math.floor((l/b))))
    index2 = SearchTableJ(table, b*(math.floor(((l+c)/b))))
    f_l, f_lc = f(index1), f(index2)
    for i in range((l % b)-1):
        f_l = f(f_l)
    for i in range(((l+c) % b)-1):
        f_lc = f(f_lc)
    while f_l != f_lc:
        l = l+1
        f_l = f(f_l)
        f_lc = f(f_lc)
    return l, c


(y, i, j) = DetectCycle(sequence[0], f)
(l, c) = RecoverCycle(f, y, i, j)
table = Sort_Dict(table)
print("cycle", c, "leader", l)
if flag:
    for i in table:
        print(i, table[i])
