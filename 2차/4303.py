import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
 
 
q_list = [[1,0]]
visited = []

while q_list:
    k = q_list.pop(0)
    start = k[0]
    cnt = k[1]
    
    if cnt > 2:
        continue
    
    if start != 1:
        visited.append(start)
      
    for n in graph[start]:
        if n not in visited and n != 1: 
            q_list.insert(0,[n,cnt+1])
            
            
 
'''
 def dfs(start, depth, visited = []):
    
    if depth <= 2:
        if start != 1:
            visited.append(start)
        
        for n in graph[start]:
            if n not in visited and n != 1:              
                dfs(n,depth+1,visited)
            
    return len(visited)

print(dfs(1,0))
 
 '''       

            
    
print(len(set(visited)))
    
