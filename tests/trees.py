import unittest
from context import trees as t

class TreesTest(unittest.TestCase):
    def setUp(self):
        self.BST = t.BST()
        self.BST.addNum(4)
        self.BST.addNum(8)
        self.BST.addNum(3)

    def test_BST_add(self):
        self.BST.process_inorder
        self.assertEqual(self.BST.size(),3)

    def test_find_kth(self):
        first = self.BST.find_kth(1)
        last = self.BST.find_kth(3)
        self.assertEqual(first,3)
        self.assertEqual(last,8)

    def test_BST_median(self):
        res = self.BST.median()
        self.assertEqual(res,4)
        self.BST.addNum(5)
        res = self.BST.median()
        self.assertEqual(res,4.5)



if __name__ == '__main__':
    unittest.main()
