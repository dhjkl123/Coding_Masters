import sys

cnt = int(sys.stdin.readline())
dic = []
ans = ''

for i in range(cnt):
    name, score = map(str,sys.stdin.readline().rstrip().split())
    dic.append([name, score])

dic_result = sorted(dic, key=lambda x: int(x[1]),reverse=True)

for dic in dic_result:
    ans += dic[0] + ' '
    
print(ans)


