import sys
from collections import deque

N,M = map(int,sys.stdin.readline().rstrip().split())

map_list = []
check_list = []

for i in range(N):
    
    tmp = sys.stdin.readline().rstrip()
    tmp_list =[]
    for t in tmp :
        tmp_list.append(int(t))
    
    map_list.append(tmp_list)
    check_list.append([0]*M)


dx = [0,0,1,-1]
dy = [-1,1,0,0]
check_list[0][0] = 1

queue = deque([[0,0]])

while queue:
    k = queue.popleft()
    x,y = k[0], k[1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if M <= nx or 0 > nx : continue
        if N <= ny or 0 > ny : continue
        
        if map_list[ny][nx] == 0 : continue
        if check_list[ny][nx] != 0 : continue
        
        check_list[ny][nx] += check_list[y][x] +1
        queue.append([nx,ny])
        
        
print(check_list[N-1][M-1])
        
    
    
    
