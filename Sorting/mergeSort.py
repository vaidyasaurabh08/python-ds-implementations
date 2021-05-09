
import time

def mergeSort(arr: list) -> list:
    if len(arr) <= 1: return arr

    mid = len(arr) // 2
    leftArr = arr[: mid]
    rightArr = arr[mid :]

    leftArr = mergeSort(leftArr)
    rightArr = mergeSort(rightArr)

    answerArr = []

    i = j = 0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] <= rightArr[j]: 
            answerArr.append(leftArr[i])
            i += 1
        else:
            answerArr.append(rightArr[j])
            j += 1


    while i < len(leftArr):
        answerArr.append(leftArr[i])
        i += 1

    while j < len(rightArr):
        answerArr.append(rightArr[j])
        j += 1
    
    return answerArr

#print(mergeSort([1,2]))

start = time.time()
print(mergeSort([5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3, 
5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3])) 
end = time.time()

print((end - start) * 10**3)