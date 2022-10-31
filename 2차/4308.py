import sys

N = int(sys.stdin.readline())

ans = 1

if N != 1:
    for i in range(2, int(N ** 0.5) +1): 
        if N % i != 0:
            continue
        else :
            ans = 0    
else:
    ans = 0
                
print(ans)