import sys

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for i in range(1,N+1):
    line = sys.stdin.readline().rstrip()
    
    for j,l in enumerate(line):
        if l == 'Y':
            graph[i].append(j+1)
            

def dfs(graph,start, cnt, visited=[]):
    
    visited.append(start)
    
    for n in graph[start]:
        if n not in visited:
            cnt = dfs(graph,n,cnt+1)
        
    return cnt
    
print(dfs(graph,1,0))
    