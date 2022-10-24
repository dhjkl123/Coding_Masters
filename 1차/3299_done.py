import sys

A,N = map(int,sys.stdin.readline().split())
t = int(sys.stdin.readline())

lst = [0] * (A+2)
lst[N] = 1

ans = 0

for i in range(0,t):
    X,Y = map(int,sys.stdin.readline().split())
    
    if lst[X] == 1 or lst[Y] == 1:
        lst[X] = 1
        lst[Y] = 1
 
        
        
print(lst.count(1))
        
