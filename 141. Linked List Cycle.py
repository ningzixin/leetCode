# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ll = []
        while head != None:
            ll.append(id(head))
            head = head.next
            if id(head) in ll:
                return True
        return False

T = ListNode(2)
T.next = ListNode(3)
print(Solution().hasCycle(T))