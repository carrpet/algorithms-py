## takes a list of keys and returns a heap

class MyMaxHeap():

    ## constructor takes a list of items (integer keys) and returns a heap
    def __init__(self,items):
        self.__data__ = []
        for item in items:
            self.__insert__(item)

    #return the index of the parent
    def __parent__(self, index):
        if index <= 0:
            return None
        else:
            return (index - 1) // 2

    ## swaps elements with the item in index
    ## until the heap order is preserved
    def __bubble_up__(self,index):
        parentIndex  = self.__parent__(index)
        if parentIndex == None:
            return

        ## in a max heap the parent is always greater than the children
        if self.__data__[parentIndex] < self.__data__[index]:
            self.__swap__(parentIndex,index)
            self.__bubble_up__(parentIndex)

    def __bubble_down__(self,index):
        child_index = self.__find_max_child_index__(index)
        if child_index == -1:
            return
        elif self.__data__[index] < self.__data__[child_index]:
            self.__swap__(index,child_index)
            self.__bubble_down__(child_index)


    def __swap__(self,i,j):
        temp = self.__data__[i]
        self.__data__[i] = self.__data__[j]
        self.__data__[j] = temp

    def __find_max_child_index__(self,index) -> int:
        c1 = 2*index + 1
        c2 = 2*index + 2
        ## in this case there are no children
        if c1 >= len(self.__data__):
            return -1
        ## in this case there is only one child so return it
        elif c2 >= len(self.__data__):
            return c1
        else:
            x = self.__data__[c1]
            y = self.__data__[c2]
            z = max(x,y)
            if z == x:
                return c1
            else:
                return c2


    def __insert__(self, item):
        self.__data__.append(item)
        self.__bubble_up__(len(self.__data__) - 1)

    def printHeap(self):
        print(self.__data__)

    def extractMax(self) -> int:
        if len(self.__data__) == 0:
            raise Exception("heap is empty, cannot extract anything")
        ans = self.__data__[0]
        toReplace = self.__data__.pop()
        if len(self.__data__) == 0:
            return ans
        self.__data__[0] = toReplace
        self.__bubble_down__(0)
        return ans
