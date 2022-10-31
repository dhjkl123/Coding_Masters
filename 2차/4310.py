import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

dalgona = [[] for _ in range(N)]
check = [[] for _ in range(N)]

for i in range(len(dalgona)):
    for _ in range(M):
        dalgona[i].append(0)
        check[i].append(0)
        
        
for i in range(N):
    line = sys.stdin.readline().rstrip()
    
    for j,l in enumerate(line):
        dalgona[i][j] = int(l)
        


dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = 0

for i in range(N):
    for j in range(M):

        if dalgona[i][j] != 0:
            continue
        
        if check[i][j] != 0:
            continue
        
        check[i][j] = 1
        q = [[j,i]]
        cnt += 1
        
        while len(q) > 0:
            tmp = q.pop(0)
            x = tmp[0]
            y = tmp[1]

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if nx < 0 or nx >= M : continue
                if ny < 0 or ny >= N : continue
                
                if check[ny][nx] != 0 : continue
                if dalgona[ny][nx] != 0: continue
                
                q.insert(0,[nx,ny])
                check[ny][nx] = 1
                
    
print(cnt)   
    
    




