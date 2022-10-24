import sys

n,a,b,c = map(int,sys.stdin.readline().split())

xpos = []
ypos = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

lst = []
for i in range(0,n):
    lst.append([0]*n)

for i in range(0,a):
    x,y = map(int,sys.stdin.readline().split())
    lst[x-1][y-1] = -1
    
    
    for k in range(0,4):
        for j in range(1,b+1):
            
            nx = (x-1) + dx[k]*j
            ny = (y-1) + dy[k]*j

            
            if nx < 0 or nx >= n : continue
            if ny < 0 or ny >= n : continue
            if lst[nx][ny] == -1 : continue
            
            lst[nx][ny] += 1
          
          
cnt = 0

for i in range(0,n):
    for j in range(0,n):
        if lst[i][j] >= c:
            cnt += 1

print(cnt)