import sys 
input = sys.stdin.readline

n = int(input())

result = {} # result 딕셔너리 생성 

for i in range (n):
    words = input().strip()
    length = len(words)
    if length not in result : 
        result[length]=[]
    result[length].append(words)

# key 값 기준으로 정렬 
for key in sorted(result.keys()):
    # key 에 해당하는 value 값 하나인 경우 그대로 출력력
    if len(result[key])==1 : 
        print(result[key][0])

    # key 에 해당하는 value 값 여러개 => 정렬 후 출력력
    else : 
        values = sorted(set(result[key])) #중복된 단어 제거 
        for value in values:
            print(value)
