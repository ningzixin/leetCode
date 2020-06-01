# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        while head.val == val:
            if head != None:
                head = head.next
                if head == None:
                    break
            else:
                break
        if head == None:
            return None
        bef = head
        if head.next != None:
            no = head.next
        else:
            return head
        while no != None:
            if no.val == val:
                no = no.next
                bef.next = no
                continue
            else:
                no = no.next
                bef = bef.next
        return head
T = ListNode(1)

S = Solution().removeElements(T,2)
while S!= None:
    print(S.val)
    S = S.next