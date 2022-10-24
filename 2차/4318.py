import sys

N = int(sys.stdin.readline())
lst = sorted(list(map(int,sys.stdin.readline().rstrip().split())),reverse=True)

sum = []

for i,l in enumerate(lst):
    sum.append(l*(i+1))
        

print(max(sum))