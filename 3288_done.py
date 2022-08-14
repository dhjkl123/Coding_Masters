import sys

t = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

lst_cnt = [0] * 11

max_val = 0

for i in range(1,11):
    lst_cnt[i] = lst.count(i)
    
    
for i in range(1,11):
    if lst_cnt[i] >=2:
        if lst_cnt[i] % 2: #홀수개
            lst_cnt[i] = lst_cnt[i] - (lst_cnt[i] % 2)
        else: #짝수개
            if (lst_cnt[i] // 2) % 2 and (lst_cnt[i] // 2) > 2: # 2쌍이 3개 이상 홀수개
                lst_cnt[i] -= 2           
                max_val = max(max_val, i* i)
            elif (lst_cnt[i] // 2) % 2 == 0:
                max_val = max(max_val, i* i)
                            
        for j in range(i+1,11):
            if lst_cnt[j] >= 2:
                max_val = max(max_val, i* j)
                
                
print(max_val)
