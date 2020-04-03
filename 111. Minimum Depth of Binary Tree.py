# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class CopyNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

    def getHight(self,root):
        if root.left != None:
            self.getHight(root.left)
        if root.right != None:
            self.getHight(root.right)
        if root.left == None and root.right == None:
            root.hight = 0
        if root.left == None and root.right != None:
            root.hight = root.right.hight + 1
        if root.left != None and root.right == None:
            root.hight = root.left.hight + 1
        if root.left != None and root.right != None:
            root.hight = max(root.left.hight, root.right.hight) + 1

    def level(self,T):
        q = []
        q.append(T)
        T.vall = 0
        while len(q) != 0:
            T = q[0]
            q.pop(0)
            if T.left == None and T.right == None:
                return (T.vall)
            if T.left != None:
                q.append(T.left)
                T.left.vall = T.vall + 1
            if T.right != None:
                q.append(T.right)
                T.right.vall = T.vall + 1
T = CopyNode(1)
T.left =CopyNode(2)
T.right = CopyNode(3)
T.left.left = CopyNode(4)
T.left.right = CopyNode(5)
T.right.right = CopyNode(6)
T.left.left.left = CopyNode(7)
T.right.right.right = CopyNode(8)
print(Solution().level(T)+1)