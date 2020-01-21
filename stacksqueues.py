class StackWithMin:
    def __init__(self):
        self.__top = -1
        self.__data = []
        self.__minIndex = None

    def pop(self):
        if self.isEmpty():
            throw Exception()
        oldTop = self.__top
        self.__top = self.__top - 1
        return __data[oldTop]

    def peek(self):
        if self.isEmpty():
          throw Exception()
        return __data[self__top]

    def push(self,item):
        __data.append(item)
        self.__top = self.__top + 1
        if self.__minIndex is None or item < self.__data[self.__minIndex]:
            self.__minIndex = self.__top


    def min(self):
        if self.isEmpty():
            throw Exception()
        return self.__data[self.__minIndex]

      def isEmpty(self):
        if self.__top == -1:
          return True
        return False
