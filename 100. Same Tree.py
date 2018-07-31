# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    flag = True
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        Solution.isSame(self,q,p)
        return  Solution.flag
    def isSame(self,p,q):
        try:
            if p.val != q.val:
                Solution.flag = False
        except:
            if not (p is None and q is None):
                Solution.flag = False
            return
        Solution.isSameTree(self, p.left, q.left)
        Solution.isSameTree(self, p.right, q.right)
q = TreeNode(0)
p = TreeNode(0)
q1 = TreeNode(1)
q.right = q1
print(Solution.isSameTree("",q,p))