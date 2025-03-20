#후보 추천하기 
import sys
input = sys.stdin.readline

N = int(input()) # 사진틀 개수 
T = int(input()) # 전체 추천 개수 

students = list(map(int, input().split())) # 추천받은 학생들  

count = {} # 딕셔너리로 설정 
frame = []

for student in students:
    if student in frame: 
        count[student] += 1

    else: 
        if len(frame) >= N:
            # 1. 추천수 작은 것 -> 2. 가장 오래된 후보 삭제 
            cnt = list(count.values())
            min_cnt = min(cnt)
            for stu in frame: 
                if count[stu] == min_cnt:
                    frame.remove(stu)
                    del count[stu]
                    break 

        frame.append(student)
        count[student] =  1


print(' '.join(map(str, sorted(frame))))
# 또 다른 출력 방법 : print(*sorted(frame))
            
            