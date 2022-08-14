import sys

t = int(sys.stdin.readline())
lst = list(sys.stdin.readline().rstrip())

cnt = 0

# P : 선풍기
# S : 시원한 학생

for i in range(0,len(lst)):
    if i != 0 and i != len(lst)-1:
        if lst[i] == 'X':
            if lst[i-1] == 'O' and lst[i+1] == 'O':
                cnt += 1
                lst[i] = 'P'
                lst[i-1] = 'S'
                lst[i+1] = 'S'
            
            
for i in range(0,len(lst)):
    if lst[i] == 'X':
        if i == 0 :
            if lst[i+1] == 'O':
                cnt += 1
                lst[i] = 'P'
                lst[i+1] ='S'
        elif i == len(lst)-1:
            if lst[i-1] == 'O':
                cnt += 1
                lst[i] = 'P'
                lst[i-1] = 'S'
        else:
            if lst[i+1] == 'O':
                cnt += 1
                lst[i] = 'P'
                lst[i+1] = 'S'
            elif lst[i-1] == 'O':
                cnt += 1
                lst[i] = 'P'
                lst[i-1] = 'S'
        
print(cnt)
        