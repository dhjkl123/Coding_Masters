# -*- coding: utf-8 -*-
import sys

a = int(sys.stdin.readline())

lst = [[[1]]]


for i in range(1,a): #층
    tmp_lst = []
    col = 0
    for j in range(0,i+1): #행
        col += 1
        row_lst = []
        for k in range(0,col):
            tmp1, tmp2, tmp3, tmp4 = 0,0,0,0

            if len(lst[i-1])>j and len(lst[i-1][j])>k:
                tmp1 = lst[i-1][j][k] 
                
            if j-1 >= 0:
                if len(lst[i-1])>j-1 and len(lst[i-1][j-1])>k :
                    tmp2 = lst[i-1][j-1][k] 
            
            if k-1 >= 0:
                if len(lst[i-1])>j and len(lst[i-1][j])>k-1 :
                    tmp3 = lst[i-1][j][k-1]
            
            if j-1 >= 0 and k-1 >= 0: #elif 로 바꿔봐
                if len(lst[i-1])>j-1 and len(lst[i-1][j-1])>k-1 :
                    tmp4 = lst[i-1][j-1][k-1]

            s = tmp1+tmp2+tmp3+tmp4
            
            if s:
                row_lst.append(tmp1+tmp2+tmp3+tmp4)
        tmp_lst.append(row_lst)
    lst.append(tmp_lst)        
    
    
print(lst)