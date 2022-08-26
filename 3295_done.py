import sys

a = sys.stdin.readline().rstrip()

char = ''
uint = ''

for ch in a:
    if ch >= 'A' and ch <= 'Z':
        char += ch
    else:
        uint += ch
   
ans_tmp = ''

if char[len(char)-1] == 'A':
    if char.count('A') == len(char) : # 전부 A
        for i in range(0,len(char)-1):
            ans_tmp += 'Z'
    elif char[len(char)-2] == 'A':
        ans_tmp += char[0]
        ans_tmp += 'Z'
    else :
        if len(char) == 3:
            ans_tmp += char[0]
            ans_tmp += chr(ord(char[len(char)-2]) - 1)
            ans_tmp += 'Z'
        else :
            ans_tmp += chr(ord(char[len(char)-2]) - 1)
            ans_tmp += 'Z'
        
else :
    for i in range(0,len(char)-1):
        ans_tmp += char[i]
    
    ans_tmp += chr(ord(char[len(char)-1]) - 1)

ans_left = ans_tmp + uint
print(ans_left)

ans_up = char + str(int(uint) - 1)        
print(ans_up)

