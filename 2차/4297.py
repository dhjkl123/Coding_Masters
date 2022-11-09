import sys

N = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().rstrip().split()))

lst_tmp = sorted(lst,reverse=True)

dic={}

cnt = 1

for i in lst_tmp:
    if i not in dic:
        dic[i] = cnt
    cnt += 1

for e in lst:
    print(e, dic[e])