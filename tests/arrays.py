import unittest
from context import arrays as a

class ArraysTest(unittest.TestCase):
    def setUp(self):
        self.arr = [5,4,3,2]
    def test_find_min_index(self):
        #arr = [5,4,3,2]
        result = a.findMinIndex(self.arr)
        self.assertEqual(result,3)

    def test_swap(self):
        #arr = [5,4,3,2]
        a.swap(1,3,self.arr)

        ## this should print [5,2,3,4]
        #print(arr)
    def test_selection_sort(self):
        a.selection_sort(self.arr)


if __name__ == '__main__':
    unittest.main()
