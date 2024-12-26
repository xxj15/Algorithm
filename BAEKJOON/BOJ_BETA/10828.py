import sys
input = sys.stdin.readline

n = int(input())
stack = []

 # push, top, size, empty, pop (5개)
for i in range(n):
    cmd = input().strip().split() # stdin으로 읽어오면 공백 무조건 포함됨. -> strip으로 공백 제거해줘야함 
   
    if cmd[0]=='push':
        stack.append(cmd[1])
    elif cmd[0] == 'top':
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else: # pop 
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
