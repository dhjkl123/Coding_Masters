import sys

t = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))

lst_ans = sorted(lst)

min_len = 10

for i in range(0,len(lst)):
    lst_tmp = []
    if i != 0:
        lst_tmp = lst[:i]
    for j in range(i+1,len(lst)+1):
        lst_tmp1 = sorted(lst[i:j])
        lst_tmp2 = lst[j:]
        lst_tmp += lst_tmp1 + lst_tmp2
        
        f = True
        for k in range(0,len(lst_tmp)):
            if lst_tmp[k] != lst_ans[k]:
                f = False
                lst_tmp = lst[:i]
                break
        
        if f:
            min_len = min(j-i,min_len)
            lst_tmp = lst[:i]
            
            
print(min_len)
                
                
            
        
        