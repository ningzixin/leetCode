# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        T = ListNode(0)
        ne = head.next
        while head!=None:
            temp = T.next
            T.next = head
            head.next = temp
            head = ne
            if head != None:
                ne = head.next
        return T.next
# T= ListNode(1)
# T.next = ListNode(2)
# T.next.next = ListNode(3)
# T.next.next.next = ListNode(4)

S = Solution().reverseList(T)
while S!= None:
    print(S.val)
    S = S.next