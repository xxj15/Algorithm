#분해합 
import sys
input = sys.stdin.readline

M = int(input())

for num in range(1, M+1):
    M_sum = 0 
    for digit in str(num):
        M_sum += int(digit)
    
    if M_sum + num == M : 
        print(num)
        exit(0)

    
print(0)
  