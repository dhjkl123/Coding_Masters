import sys

N,M = map(int,sys.stdin.readline().split())

lst = []

for i in range(0,N):
    tmp_lst = list(map(int,sys.stdin.readline().split()))
    lst.append(tmp_lst)
    

dx = [1,-1,0,0]
dy = [0,0,1,-1]

max_score = 0

for i in range(0,N):   
    for j in range(0,M):
        score = 0
        score += lst[i][j]
        
        for k in range(0,4):
            ny = i + dy[k]
            nx = j + dx[k]
            
            if ny < 0 or ny >= N: continue
            if nx < 0 or nx >= M: continue
            
            score += lst[ny][nx]
        
        max_score = max(score,max_score)
        

print(max_score)
            