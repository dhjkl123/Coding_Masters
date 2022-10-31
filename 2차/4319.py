import sys
from collections import Counter
N = int(sys.stdin.readline())

lst = []

for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()

cnt_lst = Counter(lst)
cnt_lst = cnt_lst.most_common()[0]

print(cnt_lst[0])
