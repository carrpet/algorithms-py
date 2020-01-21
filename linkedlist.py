##remove duplicates from an unsorted singly linked list
## how would you do this if no temporary buffer is allowed
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    try:
        iter(x)
        if len(x) == 1:
            self.val = x[0]
            self.next = None
            return
        listnodes = [ListNode(x) for x in x[1:]]
        for i,node in enumerate(listnodes):
            if i == len(listnodes) - 1:
                break
            node.next = listnodes[i + 1]
        printList(listnodes[0])
        self.val = x[0]
        self.next = listnodes[0]

    except TypeError:
        self.val = x
        self.next = None

def printList(ll: ListNode):
    contents = []
    while ll != None:
        contents.append(ll.val)
        ll = ll.next
    print(contents)

def listContains(ll: ListNode, item) -> bool:
    while ll != None:
        if ll.val == item:
            return True
        ll = ll.next
    return False

## takes a pointer to a linked list and a value and removes it
def removeListItem(ll: ListNode, item) -> ListNode:
    listhead = ll
    if ll == None:
        return None

    # case where item is first TreeNode
    if ll.val == item:
        if ll.next == None:
            return None
        else:
            return ll.next

    while ll != None and ll.next != None:
        if ll.next.val == item:
            ll.next = ll.next.next
        ll = ll.next
    return listhead


# with a temporary buffer
# maintain a dictionary of <item,
def removeDups(ll: ListNode) -> ListNode:
    head = ll
    seen = set()
    if ll == None or ll.next == None:
        return ll

    while ll != None:
        seen.add(ll.val)
        if ll.next and ll.next.val in seen:
            ll.next = ll.next.next
        ll = ll.next

    return head


    #
    # dups = {}
    # while ll != None:
    #     if not ll.val in dups:
    #         dups[ll.val] = 1
    #     else:
    #         dups[ll.val] = dups[ll.val] + 1
    #     ll = ll.next
    # while head != None:
    #     d = dups[head.val]
    #     if d > 1:
    #         p = head
    #         while d > 1:
    #             if p.val
