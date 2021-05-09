import time

def insertionSort(arr: list)-> list:
    for i in range (1, len(arr)):
        key = arr[i]
        j = i - 1
        while arr[j] > key and j >= 0:
            # tmp = arr[j]
            # arr[j] = arr[j+1]
            arr[j+1] = arr[j]

            j -= 1
        
        arr[j+1] = key

    return arr

start = time.time()
print(insertionSort([5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3, 
5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3, 5,2,4,6,1,3])) 
end = time.time()

print((end - start) * 10**3)
