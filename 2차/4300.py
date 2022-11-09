import sys

A, B = map(int,sys.stdin.readline().rstrip().split())
N, M = map(int,sys.stdin.readline().rstrip().split())

lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
    
lst.sort(reverse=True)

print(A+B*(sum(lst[:M])))