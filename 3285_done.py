import sys

t = int(sys.stdin.readline())

a,b = map(int,sys.stdin.readline().split())

min_d = 1000000000

for i in range(0,t):
    x,y = map(int,sys.stdin.readline().split())
    
    d = abs(a-x) + abs(b-y)
    
    min_d = min(d,min_d)
    

print(min_d*100)