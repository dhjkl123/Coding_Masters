import sys
from decimal import Decimal
import decimal

p,q = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())

decimal.getcontext().prec = n

ans = (Decimal(p)/Decimal(q))

ans = Decimal(round(ans,n))

if len(str(ans)) < n+2:
    print(f'%.{n}f'%ans)
else :
    print(ans)
