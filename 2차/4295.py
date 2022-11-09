import sys

N = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().rstrip().split()))

for i in lst:
    print(i,end=' ')
    
print()

for i in range(N-1):
    tmp = lst.pop(0)
    lst.append(tmp)
    
    for j in lst:
        print(j,end=' ')
    print()
    