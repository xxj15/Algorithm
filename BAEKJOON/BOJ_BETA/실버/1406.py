import sys
input= sys.stdin.readline

str1=list(input().strip())
n = int(input())
str2 = []

for i in range (n):
    cmd = input().strip().split()
    if cmd[0] == 'L':
        if len(str1)>0:
            str2.append(str1.pop())
    elif cmd[0]=='D':
        if len(str2)>0:
            str1.append(str2.pop())
    elif cmd[0]=='B':
        if len(str1)>0:
            str1.pop()
    else : 
        str1.append(cmd[1])
print(''.join(str1 + str2[::-1]))


'''
str = input().strip()
n = int(input())
cursor = len(str)


# L, D, B, P 
for i in range(n):
    cmd = input().strip().split()
    if cmd [0] == 'L': 
        if cursor > 0:
            cursor -= 1
    elif cmd[0]=='D':
        if cursor < len(str):
            cursor += 1 
    elif cmd[0]=='B':
        if cursor>0:
            if len(str)== cursor : 
                str = str[:cursor-1]
                cursor -= 1
            else : 
                str = str[:cursor-1]+str[cursor:]
                cursor -= 1
    else: # cmd[0] =='P'
        if len(str)==cursor: 
            str = str + cmd[1]
            cursor += 1
        elif cursor ==0 :
            str = cmd[1]+str[cursor:]
            cursor+=1
        else: 
            str = str[:cursor]+cmd[1]+str[cursor:]
            cursor+=1

print(str)
'''
