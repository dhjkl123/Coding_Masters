import sys

res_list = [99999999]



def func(x,cnt):
    
    if cnt >= min(res_list):
        return
    
    if x == 1:
        res_list.append(cnt)
        return
    
    if x % 5 == 0:
        func(x//5,cnt+1)

    if x % 3 == 0:
        func(x//3,cnt+1)
    
    if x % 2 == 0:
        func(x//2,cnt+1)
    
    if x - 1 >= 1:
        func(x-1,cnt+1)
        


X = int(sys.stdin.readline())

func(X,0)

print(min(res_list))


