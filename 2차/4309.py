import sys

N = int(sys.stdin.readline())

A = []

for i in range(N):
    a= int(sys.stdin.readline())
    A.append(a)
      
B,C = map(int,sys.stdin.readline().rstrip().split())

ans_list = []

for a in A:
    tmp = a
    cnt = 0
    bspecial = True
    
    while tmp > 0:
        if bspecial:
            tmp -= B
            bspecial = False
        else:
            tmp -= C
        cnt += 1
    ans_list.append(cnt)
    
print(sum(ans_list))
    
        