import sys 
input = sys.stdin.readline 

n = int(input())

for i in range(n):
    stack = []
    a = input().strip() # strip - 문자열의 시작과 끝에서 주어진 문자를 제거 (안해서 처음에 틀림)
    
    for x in a : # 문자열에 있는 문자 하나씩 검사 
        if x == '(':
            stack.append(x)
        else : 
            if not stack : # empty 이면 
                print("NO")
                break
            else : 
                stack.pop() 
    
    # break 문으로 안나가고 전체 문자 검사한 경우
    else: 
        if not stack : # 남아있는 스택이 비어있음 
            print("YES")
        else : 
            print("NO")
        

        