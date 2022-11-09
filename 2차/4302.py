import sys

N = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().rstrip().split()))

a,b = map(int,sys.stdin.readline().rstrip().split())

res_lst = lst[a-1:b]

print(min(res_lst))