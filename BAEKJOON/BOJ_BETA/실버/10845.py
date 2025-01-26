import sys 
input = sys.stdin.readline

n = int(input())

# push, front, back, size, empty, pop 

queue = []

for i in range(n):
    cmd = input().strip().split() 
   
    if cmd[0]=='push':
        queue.append(cmd[1])
    elif cmd[0] == 'front':
        if len(queue)!=0:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(queue)!=0:
            print(queue[-1])
        else:
            print(-1)        
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    else: # pop 
        if len(queue)==0: 
            print(-1)
        else:
            print(queue.pop(0)) # pop 함수 : 문자열에서 특정 위치에 있는 문자를 제거하고 반환하는 기능
