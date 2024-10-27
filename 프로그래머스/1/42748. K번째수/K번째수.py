def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        arr1 = array[i-1:j]
        arr1.sort()
        answer.append(arr1[k-1])
    
    return answer