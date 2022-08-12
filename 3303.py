import sys

def func(a,now,lim):
    hlst = [0] * a
    hlst[0], hlst[a-1] = 1,1

    term = now
    pos = 0
    
    
    
    # 1 0 0 0 0 1 0 0 0 1 | 10 20 5 2 일때 말뚝의 간격이 모두 만족 더 이상 할 필요 없음
    # 1 0 0 1 0 0 0 1 | 8 8 3 2 일 때 말뚝의 간격중 최소 간격을 만족을 못함
    
    
    while pos < a:
        hlst[pos] = 1
        
        if a-1 - pos > now : # 
            if pos + term > a-1 - lim: #다음 위치가 최소 범위 밖
                term = lim

        elif a-1 - pos <= now: # 현재 범위 안
            break
        
        
        pos += term
    

    
    return hlst.count(1)


a,b,D,d = map(int,sys.stdin.readline().split())

res_min = 0
res_max = 0

if (a > d or a == 1)  and (b > d or b == 1):
 
    tmp = func(a,d,d)
    res_max += tmp * 2 
    tmp = func(b,d,d) - 2
    res_max += tmp * 2

    tmp = func(a,D,d)
    res_min += tmp * 2
    tmp = func(b,D,d) - 2
    res_min += tmp * 2
    

    
    print(res_min, res_max)
else:
    print('-1')
    
    
