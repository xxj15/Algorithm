n = int(input())
arr1 = list(map(int,input().split()))

m = int(input())
arr2 = list(map(int,input().split()))
arr1.sort()

for x in arr2:
    left =0 
    right = n-1 
    inArr = False

    while left <= right: 
        mid = (left+right)//2
        if x == arr1[mid]:
            print(1)
            inArr = True
            break
        elif x < arr1[mid]:
            right = mid-1
        else :
            left = mid + 1

    if inArr == False:
        print(0)
        