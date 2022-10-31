import sys

N = int(sys.stdin.readline())

D = [0] * 1000
D[1] = 1
D[2] = 3


for i in range(3,N+1):
    D[i] = D[i - 1] + (D[i - 2]*2)
        

print(D[N] % 796796)