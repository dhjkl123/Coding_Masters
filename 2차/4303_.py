import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(start, depth, visited = []):
    
    if depth <= 2:
        if start != 1:
            visited.append(start)
        
        for n in graph[start]:
            if n not in visited and n != 1:              
                dfs(n,depth+1,visited)
            
    return len(visited)
            
    
print(dfs(1,0))
    
