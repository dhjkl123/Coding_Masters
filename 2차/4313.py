import sys

N = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().rstrip().split()))

boodae_lst = [ [] for _ in range(N+1)]

for i,l in enumerate(lst):
    boodae_lst[l].append(i+1)

def dfs(start,t, max_depth):
       
    for boodae in boodae_lst[start]:
        if boodae == start:
            continue
        
        max_depth = dfs(boodae,t+1,max_depth)
    
    return max(max_depth , t)
                

    
ans = dfs(1,0,0)

print(ans)
