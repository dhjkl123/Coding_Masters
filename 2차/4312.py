import sys

N,K = map(int,sys.stdin.readline().split())

lst = []

for _ in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))

w_lst =[]
    
for _ in range(K):
    w_lst.append(int(sys.stdin.readline()))
    
lst.sort(reverse=True,key=lambda x : x[1])
w_lst.sort()

res = 0

check = []

for w in w_lst:
    for i in range(N):
        if i in check : continue
        
        if w >= lst[i][0]:
            res += lst[i][1]
            check.append(i)
            break
            
            
            
            
print(res)
        