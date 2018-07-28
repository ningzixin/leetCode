# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        q = head

        while head!=None:
            p = head.next
            if(p!=None and head.val == p.val):
                head.next = head.next.next
                continue
            head = head.next
        return q
ll1 = ListNode(1)
ll2 = ListNode(1)
ll3 = ListNode(1)
ll1.next = ll2
ll2.next = ll3
ll = Solution.deleteDuplicates("",ll1)
while ll != None:
    print(ll.val)
    ll = ll.next