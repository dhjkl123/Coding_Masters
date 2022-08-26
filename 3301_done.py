import sys

y, m, b, c = map(str,sys.stdin.readline().rstrip().split())

# y : 년차
# m : 소속 육 : ROKA , 해 : ROKN, 공 : ROKAF
# b : 지정여부 Y : 동원지정 , N : 미지정
# c : 신분 Private : 병 , Officer : 간부

y = int(y)

if c == 'Private':
    if y == 0 :
        print('0')
    elif y >= 1 and 4 >= y:
        if b == 'N':
            if m == 'ROKAF':
                print(28)
            else :
                print(32)
        else:
            print(28)
    elif y >= 5 and y <= 6:
        print(20)

else :
    if y == 0 :
        print('0')
    elif y >= 1 and y <= 6:
        print(28)
        
    