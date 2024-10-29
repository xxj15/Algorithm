'''
시간초과 답안 
n = int(input())

cnt = 1 
start_idx = 1 
end_idx = 1
sum = 1

while end_idx < n : 
    if sum < n:
        end_idx += 1
        sum += end_idx
    elif sum > n : 
        start_idx += 1
        end_idx = start_idx
        sum = start_idx
    else : 
        cnt += 1 
        start_idx += 1 
        end_idx = start_idx
        sum = start_idx
        
print(cnt)
        
'''

n = int(input())

cnt = 1 
start_idx = 1 
end_idx = 1
sum = 1

while end_idx < n : 
    if sum < n :
        end_idx += 1
        sum += end_idx
    elif sum == n : 
        cnt += 1 
        end_idx += 1 
        sum += end_idx
    else : 
        sum -= start_idx
        start_idx += 1 
        
print(cnt)