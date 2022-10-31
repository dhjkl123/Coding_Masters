import sys

N,M = map(int,sys.stdin.readline().split())

n_from_list = []
n_to_list = []

for line in range(M):
    n_from, n_to = map(int,sys.stdin.readline().split())
    n_from_list.append(n_from)
    n_to_list.append(n_to)

check = []

for i in range(N+1):
    check.append([])

stack_list = [i for i in range(N,0,-1)]


while len(stack_list) > 0:
    k = stack_list.pop()

    for i,n_from in enumerate(n_from_list):
        if n_from == k:
            
            if n_to_list[i] not in check[k]:
                check[k].append(n_to_list[i])
                stack_list.append(n_to_list[i])
                
            if k not in check[n_to_list[i]]:
                check[n_to_list[i]].append(k)
                
            
for i,line in enumerate(check):
    ans = ''
    
    if i == 0:
        continue
    
    if len(line) == 0:
         print('no')
    else:
        line.sort()
        for l in line:
            ans += str(l) + ' '
        
        print(ans)
    
