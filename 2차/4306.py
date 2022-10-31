import sys

N,M,K = map(int,sys.stdin.readline().rstrip().split())

map_list = []
check_list = []

for i in range(N):
    map_list.append([])
    check_list.append([])
    for _ in range(M):
        map_list[i].append(0)
        check_list[i].append(0)
        
for _ in range(K):
   X,Y = map(int,sys.stdin.readline().rstrip().split())
   map_list[Y][X] = 1
   
   
q = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0

for i in range(N):
    for j in range(M):
        
        if map_list[i][j] == 1 and check_list[i][j] == 0:
            q.insert(0,[j,i])
            
            cnt += 1
            
            while len(q) > 0:
                k = q.pop(0)
                x = k[0]
                y = k[1]
                
                for t in range(4):
                    nx = x + dx[t]
                    ny = y + dy[t]
                    
                    if nx < 0 or nx >= M: continue
                    if ny < 0 or ny >= N: continue
                    
                    if check_list[ny][nx] != 0: continue
                    if map_list[ny][nx] != 1: continue
                    
                    check_list[ny][nx] = 1
                    q.insert(0,[nx,ny])
                    
print(cnt)
                                   

