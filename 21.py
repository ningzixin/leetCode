# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    ll = ListNode("")
    p = ll
    while(l1!=None or l2 != None):
        if(l1==None and l2 !=None):
            p.next = ListNode(l2.val)
            l2 = l2.next
            p = p.next
            continue
        if (l1 != None and l2 == None):
            p.next = ListNode(l1.val)
            l1 = l1.next
            p = p.next
            continue
        if(l1.val <= l2.val):
            p.next = ListNode(l1.val)
            l1 = l1.next
            p = p.next
        else:
            p.next = ListNode(l2.val)
            l2 = l2.next
            p = p.next
    return ll.next
l1 = ListNode("1")
l1.next = ListNode("2")
l1.next.next = ListNode("3");
l2 = ListNode("1")
l2.next = ListNode("2")
l2.next.next = ListNode("3");
ll = mergeTwoLists(",",l1,l2)
while ll!=None:
    print(ll.val)
    ll = ll.next