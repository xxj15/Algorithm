'''
def solution(numbers):
    answer = []
    numbers = list(map(str, numbers))
    
    while numbers:
        maxNum = numbers[0]
        for num in numbers:
            if num + maxNum > maxNum + num:
                maxNum = num
        
        answer.append(maxNum)
        numbers.remove(maxNum)
    
    result = ''.join(answer)
    return '0' if result[0] == '0' else result
'''
def sort_key(x):
    return x * 3

def solution(numbers):
    numbers = list(map(str, numbers))
    
    # 파이썬 - 문자열의 사전적 순서 
    numbers.sort(key=sort_key, reverse = True)
    
    result = ''.join(numbers) 
    return '0' if result[0] == '0' else result
