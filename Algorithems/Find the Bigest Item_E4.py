def Find_the_bigest_item(A):
    n = len(A)
    if n == 1:
        return A[0]
    
    mid = int(n/2)
    bigestItem = 0
    if A[mid-1] > A[mid]:
        bigestItem = Find_the_bigest_item(A[0:mid])
    else:    
        bigestItem = Find_the_bigest_item(A[mid:n])
    
    return bigestItem        


arr = list(map(int,input().split(',')))
bigArrItem = Find_the_bigest_item(arr)
for i in range(len(arr)):
    if arr[i] == bigArrItem:
        print(i)
        break
