import unittest

import linkedlist as ll
import heap as h
import trees as t
import dynamic as d
import sorting as s

class TestLLMethods(unittest.TestCase):

    def create_test_list(self):
        a = ll.ListNode(3)
        b = ll.ListNode(4)
        c = ll.ListNode(5)
        b.next = c
        a.next = b
        return a

    def test_remove_list_item_first(self):
        testList = self.create_test_list()
        removedList = ll.removeListItem(testList,3)
        self.assertFalse(ll.listContains(removedList, 3))

    def test_remove_list_item_second(self):
        testList = self.create_test_list()
        removedList = ll.removeListItem(testList,4)
        self.assertFalse(ll.listContains(removedList, 4))

    def test_remove_list_item_last(self):
        testList = self.create_test_list()
        removedList = ll.removeListItem(testList,5)
        self.assertFalse(ll.listContains(removedList, 5))

    def test_remove_dups(self):
        a = ll.ListNode(1)
        b = ll.ListNode(4)
        c = ll.ListNode(5)
        d = ll.ListNode(4)
        d.next = c
        c.next = b
        b.next = a
        #ll.printList(d)
        r = ll.removeDups(d)
        #print("llworks result: ")
        #ll.printList(r)
        linkd = ll.ListNode([7,1,5,5,9,0])
        #print("before")
        #ll.printList(linkd)
        result = ll.removeDups(linkd)
        #print("after")
        #ll.printList(result)

    def test_heap1(self):
        it = [1]
        heap = h.MyMaxHeap(it)
        heap.printHeap()

    def test_heap2(self):
        stuff = [2,4,5,7,110,240,351,7777]
        heap = h.MyMaxHeap(stuff)
        heap.printHeap()
        print(heap.extractMax())
        print
        heap.printHeap()

    def test_heapsort(self):
        stuff = [2,4,5,7,110,240,351,7777]
        heap = h.MyMaxHeap(stuff)
        sortedStuff = [heap.extractMax() for i in stuff]
        print(sortedStuff)

    def test_trees(self):
        myTree = t.TreeNode(5)
        x = t.TreeNode(8)
        y = t.TreeNode(9)
        myTree.left = x
        myTree.right = y
        print("trees")
        print(t.getLayers(myTree))

    def test_min_index(self):
        arr = [1,8,5,9]
        ind = s.findMinIndex(arr)
        self.assertEqual(0,ind)
        arr2 = [93,4,1,9,5,3]
        ind2 = s.findMinIndex(arr2)
        self.assertEqual(2,ind2)

    def test_swap(self):
        arr = [93,4,1,83,2]
        s.swap(0,2,arr)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[2], 93)

    def test_selection_sort(self):
        arr = [4,3,1,2]
        swaps = s.minimumSwaps(arr)
        self.assertEqual(swaps,arr)



    #def test_dynamic(self):
    #    d.maximumToys([3,4,100], 5)




if __name__ == '__main__':
    unittest.main()
