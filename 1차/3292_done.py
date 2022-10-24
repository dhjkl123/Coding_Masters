import sys

H,W = map(int,sys.stdin.readline().split())

screen = []

for i in range(0,H):
    line = list(sys.stdin.readline().rstrip())
    screen.append(line)
    
h,w = map(int,sys.stdin.readline().split())

char = []

for i in range(0,h):
    line = list(sys.stdin.readline().rstrip())
    char.append(line)
    
diff_y = H-h-1
diff_x = W-w-1
    
for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        if i > diff_y and j > diff_x:
            if char[i-(diff_y+1)][j-(diff_x+1)] != '.':
                screen[i][j] = char[i-(diff_y+1)][j-(diff_x+1)]
                
    
for e in screen:
    out = ''
    for ele in e:
        out += ele
    print(out)

