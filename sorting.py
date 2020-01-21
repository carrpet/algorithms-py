def findMinIndex(arr):
    minIndex = 0
    for i,num in enumerate(arr):
        if num < arr[minIndex]:
            minIndex = i
    return minIndex

def swap(i,j,arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def minimumSwaps(arr):
    print("in minSwaps")
    ans = 0
    for i in range(len(arr)):
        print(arr)
        minInd = i + findMinIndex(arr[i:])
        print("minIndex is")
        print(minInd)
        if minInd != i:
            swap(i,minInd,arr)
            ans += 1

    #print(arr)
    return ans
