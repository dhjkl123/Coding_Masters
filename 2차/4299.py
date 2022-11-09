import sys
from itertools import permutations

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().rstrip().split()))

p2 = list(set(permutations(lst,2)))
p3 = list(set(permutations(lst,3)))

ans = 0

for p in p2:
    tmp = 1
    for e in p:
        tmp *= e
        
    ans = max(ans, tmp)
    
for p in p3:
    tmp = 1
    for e in p:
        tmp *= e
        
    ans = max(ans, tmp)


print(ans)