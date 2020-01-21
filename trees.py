# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.__root__ = None
        self.__numNodes__ = 0

    def __insert__(self,root,node):
        if self.__numNodes__ == 0:
            self.__root__ = node
            self.__numNodes__ += 1
        elif root.left == None and node.val <= root.val:
            root.left = node
            self.__numNodes__ += 1
        elif root.right == None and node.val > root.val:
            root.right = node
            self.__numNodes__ += 1
        else:
            if node.val <= root.val:
                self.__insert__(root.left,node)
            else:
                self.__insert__(root.right,node)


    # use inorder traversal
    def __find_kth_sorted__(self,k):
        counter = 0
        ans = None
        def doit(root,k):
            if root == None:
                return

            doit(root.left,k)
            nonlocal counter
            counter += 1
            #print("kth sorted: " + str(root.val))
            #print("counter: " + str(counter))
            if counter == k:
                nonlocal ans
                ans = root.val
                #return root.val
            doit(root.right,k)
        doit(self.__root__,k)
        return ans


    def addNum(self,num):
        newNode = TreeNode(num)
        self.__insert__(self.__root__,newNode)

    def size(self):
        return self.__numNodes__


    def process_inorder(self):
        def inorder(root):
            if root == None:
                return

            inorder(root.left)
            print(root.val)
            inorder(root.right)
        inorder(self.__root__)

    def find_kth(self,k):
        return self.__find_kth_sorted__(k)

    # return the median of the BST
    def median(self):
        if self.__numNodes__ == 0:
            return None
        if self.__numNodes__ % 2 == 0:
            ind1 = self.__find_kth_sorted__(self.__numNodes__ / 2)
            ind2 = self.__find_kth_sorted__((self.__numNodes__ / 2) + 1)
            return (ind1 + ind2) / 2
        else:
            return self.__find_kth_sorted__((self.__numNodes__ + 1) / 2)





## recursive solution
def isLeaf(node: TreeNode) -> bool:
    return node.left == None and node.right == None

def isValidBST(root: TreeNode) -> bool:
    ## an empty tree or one node tree is by default a BST
    if root == null or (isLeaf(root)):
        return True
    ## base case where children are leaves
    elif isLeaf(root.left) and isLeaf(root.right):
        return (root.left.val < root.val) and (root.right.val > root.val)
     ## case where left is a leaf and right is a tree
    elif self.isLeaf(root.left) and (not self.isLeaf(root.right)):
        return (root.left.val < root.val) and self.isValidBST(root.right)
        ## case where left is a tree and right is a leaf
    elif (not self.isLeaf(root.left)) and self.isLeaf(root.right):
        return self.isValidBST(root.left) and (root.val < root.right.val)
    else:
        return root.left.val < root.val and self.isValidBST(root.left) and self.isValidBST(root.right)

def getLayers(node: TreeNode):
    if node == None:
        return
    q = deque()
    ans=[]
    q.append(node)
    i = 0
    k = 0
    while len(q) > 0:
        if i == ((2 ** k) - 1):
            thislayer = [n.val for n in q]
            if k % 2 == 1:
                thislayer.reverse()
            ans.append(thislayer)
            k = k + 1
        thisnode = q.popleft()
        if thisnode.left != None:
            q.append(thisnode.left)
        if thisnode.right != None:
            q.append(thisnode.right)
        i = i + 1
    return ans

## return a pointer to the successor
## the successor is the minimum element of the right subtree
def getNodePath(root: TreeNode,v1):
    if root.val == v1:
        return root
    else:
        if root.info > v1:
            getNodePath(root.left, v1)
