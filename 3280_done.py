import sys

a = int(sys.stdin.readline())
dic = dict()
for i in range(0,a):
    key,val = map(str,sys.stdin.readline().split())
    dic[key] = val
    
q = sys.stdin.readline().rstrip()

if q in dic:
    print(dic[q])
else :
    print(-1)