import sys

N = int(sys.stdin.readline())

dic = {}

for i in range(N):
    age,name = sys.stdin.readline().rstrip().split()
    age = int(age)
    
    dic[name] = age
    
dic_res = sorted(dic.items(),key=lambda x: int(x[1]),reverse=True)

for d in dic_res:
    print(d[0])
    