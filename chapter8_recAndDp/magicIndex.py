

def magixIndex(arr: list):
    start = 0
    end = len(arr) - 1
    while(end > start):
        midIndex = end - start // 2
        midValue = arr[midIndex]
    
        if midIndex == midValue:
            return midIndex

        if midValue < midIndex:
            start = midIndex + 1
        
        else:
            end = midIndex - 1

    return False


def magicIndexRec(arr, start=None, end=None):
    if not start and not end:
        start = 0
        end = len(arr) - 1
    print(start, end)
    if end < start: return False
    
    mid = (end + start) // 2
    print(mid)
    
    if arr[mid] == mid: return mid

    if mid < arr[mid]: end = mid
    else: start = mid
    return magicIndexRec(arr, start, end)

print(magixIndex([1,2,3,4,5,6,543]))

lst = [-10, -5, -2, 0, 4, 78, 100]

print(magicIndexRec(lst))