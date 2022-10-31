import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

A = []

tmp = 0
ans = 0
  
for _ in range(N):
    a = int(sys.stdin.readline())
    A.append(a) 

A.sort(reverse=True)    

for i in A:
    if tmp + i > M:
        continue
    
    tmp += i
    ans += 1

print(ans)
        