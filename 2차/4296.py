import sys
from decimal import *

getcontext().prec = 3

N,M = map(float,sys.stdin.readline().rstrip().split())

N,M = Decimal(N), Decimal(M)

s = int((M-N)*100)

tmp = Decimal(0.00)

for i in range(s+1):
    res = N + tmp
    print('{:.2f}'.format(res),end=' ')
    tmp += Decimal(0.01)