import sys

money, cnt = map(int,sys.stdin.readline().rstrip().split())

lst = sorted(list(map(int,sys.stdin.readline().rstrip().split())),reverse=True)

ans = 0

for l in lst:    
    if money-l < 0:
        continue
    else :
        money -= l
        ans +=1
        
print(ans)