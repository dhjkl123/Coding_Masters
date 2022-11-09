import sys
from itertools import permutations

N = int(sys.stdin.readline())

res = []
lst = []
lst += [0] * N

for i in range(N+1):

    res += set(tuple(permutations(lst,N)))
    lst.pop(0)
    lst.append(1)


res.sort()


for r in res:
    ans = str(r)
    ans = ans.replace('(','')
    ans = ans.replace(')','')
    ans = ans.replace(',','')
    ans = ans.replace(' ','')
    
    print(ans)
