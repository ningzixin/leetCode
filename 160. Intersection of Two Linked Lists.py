# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA = headA
        nodeB = headB
        countA = 0
        countB = 0
        while nodeA != None:
            countA += 1
            nodeA = nodeA.next
        while nodeB != None:
            countB += 1
            nodeB = nodeB.next
        mar = 0

        if countB > countA: #标定A 永远大
            nodeA = headB
            nodeB = headA
            mar = countB - countA
        else:
            nodeA = headA
            nodeB = headB
            mar = countA - countB
        for i in range(0,mar):
            nodeA = nodeA.next
        while nodeA != None or nodeB != None:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None


