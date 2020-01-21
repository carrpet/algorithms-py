## Selection sort
## given an array of ints, arr return a sorted array
def selection_sort(arr):
    for i in range(len(arr)):
        minIndex = i + findMinIndex(arr[i:])
        if i != minIndex:
            swap(i,minIndex, arr)
    print("selection_sort result is: ")
    print(arr)


## given an array arr return the index of the
## mininum element

##input [5,4,3,2]
def findMinIndex(arr) -> int:
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0
    ## case where len(arr) > 1
    currentMinIndex = 0
    for i,val in enumerate(arr):
        if val < arr[currentMinIndex]:
            currentMinIndex = i
    return currentMinIndex


def swap(i,j,arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
