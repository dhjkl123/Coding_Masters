import sys

N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for line in range(M):
    n_from, n_to = map(int,sys.stdin.readline().split())
    graph[n_from].append(n_to) # 이중리스트
    graph[n_to].append(n_from)

for i in range(len(graph)):
    graph[i].sort()
    
    
def dfs(graph,start, visited =[]):
        
    visited.append(start)

    for n in graph[start]:
        if n not in visited:
            dfs(graph, n, visited)
            
    return visited

result = dfs(graph,1)

for ans in result:
    print(ans, end=' ')
    

'''

'''

