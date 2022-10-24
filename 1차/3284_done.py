import sys

a = int(sys.stdin.readline())

lst = [0]
cnt = 1
for i in range(0,a):
    cmd = sys.stdin.readline().rstrip()
    
    if cmd == 'D':
        lst.insert(0,cnt)
    else:
        lst.append(cnt)
    
    cnt += 1

for i in lst:
    print(i, end=' ')
        