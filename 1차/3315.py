# 바다와 들고양이 각각 체크 2중 리스트 생성
# 바다와 들고양이 각각 큐 생성
# 바다 체크 리스트에 들고양이 체크 리스트 outer조인
# 양수 갯수 체크



import sys

n,m = map(int,sys.stdin.readline().split())

arr = []
lst_a = []
lst_b = []
qu_a = []
qu_b = []

for i in range(0,n):
    string = sys.stdin.readline().rstrip()
    arr.append(list(string))
    lst_a.append([0] * m)
    lst_b.append([0] * m)
    pos = 0
    for ch in string:
        if ch == 'o':
            qu_a.append([pos,i])
        elif  ch == 'c':
            qu_b.append([pos,i])
            
        pos += 1
        
    
a,b = map(int,sys.stdin.readline().split())


dx = [1,-1,0,0]
dy = [0,0,1,-1]



while len(qu_a) > 0:
    
    i = qu_a[0][1] # y
    j = qu_a[0][0] # x
    
    qu_a.pop(0)
    
    if lst_a[i][j] == a:
        continue
        
    for k in range(0,4):
        nx = j + dx[k]
        ny = i + dy[k]
        
        if nx < 0 or nx >= m: continue
        if ny < 0 or ny >= n: continue
         
        if lst_a[ny][nx] == 0 and arr[ny][nx] == 'g':               
            lst_a[ny][nx] += lst_a[i][j] + 1
        
            qu_a.insert(0,[nx,ny])

while len(qu_b) > 0:
    
    i = qu_b[0][1] # y
    j = qu_b[0][0] # x
    
    qu_b.pop(0)
    
    if lst_b[i][j] == b:
        continue
        
    for k in range(0,4):
        nx = j + dx[k]
        ny = i + dy[k]
        
        if nx < 0 or nx >= m: continue
        if ny < 0 or ny >= n: continue 
         
        if arr[ny][nx] != 'c' :  
            if lst_b[i][j] == 0:
                lst_b[ny][nx] = lst_b[i][j] + 1
        
                qu_b.insert(0,[nx,ny])
            elif lst_b[ny][nx] == 0 :        
                lst_b[ny][nx] += lst_b[i][j] + 1
        
                qu_b.insert(0,[nx,ny])


ans = 0                    

for i in range(0,n):
    for j in range(0,m):
        if lst_b[i][j] > 0 :
            lst_a[i][j] = -1

for i in range(0,n):   
    for j in range(0,m):   
        if lst_a[i][j] > 0:
            ans += 1
        
        
print(ans)


