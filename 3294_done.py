# 현재 연승 수, 현재 연패 수, 최장 연승 기록, 최장 연패

import sys

t = int(sys.stdin.readline())

lst = [0] * 4


for i in range(0,t):
    res = sys.stdin.readline().rstrip()
    out = ''
    if res == 'WIN':
        lst[0] += 1
        lst[1] = 0-
        lst[2] = max(lst[0],lst[2])
    else :
        lst[0] = 0
        lst[1] += 1
        lst[3] = max(lst[1],lst[3])
        
    for e in lst:
        out += str(e) + ' '
        
    print(out)
        