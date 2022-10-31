import sys
import itertools

A = int(sys.stdin.readline())

e_list = [0] * A

lst = []

for i in range(2,(A//2)+1):
    if e_list[i] == 0 and A%i == 0:
        lst.append(i)
        for j in range(2,A):
            if i*j < A:
                e_list[i*j] = 1
            else:
                break
            
ans = []

comb = itertools.combinations(lst,2)

for c in comb:
    if c[0] * c[1] == A:
        ans.append(c[0])
        ans.append(c[1])
            
if len(ans) > 0:
    print(ans[0],ans[1])
else :
    print('IMPOSSIBLE')


