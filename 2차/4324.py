import sys

N = int(sys.stdin.readline())

lst = []
res = []


for i in range(N):
    lst.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
    
for i in range(N):
    d = lst[i][0]

    sum = 0
    for j in range(N):
        sum += abs(d - lst[j][0]) * lst[j][1]        
                
    res.append(sum)
    
min_num = min(res)

print(res.index(min_num)+1)





