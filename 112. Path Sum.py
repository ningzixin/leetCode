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
    flag = False
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if sum - root.val == 0:
            print(1)
            self.flag = True
            return True
        if root.left != None:
            sum = sum - root.val
            self.hasPathSum(root.left,sum)
            sum = sum + root.val

        if root.right != None:
            sum = sum - root.val
            self.hasPathSum(root.right,sum)
            sum = sum + root.val

T = CopyNode(1)
T.left =CopyNode(2)
T.right = CopyNode(3)
T.left.left = CopyNode(4)
T.left.right = CopyNode(5)
T.right.right = CopyNode(6)
T.left.left.left = CopyNode(7)
T.right.right.right = CopyNode(8)
s = Solution()
print(s.hasPathSum(T,18))
print(s.flag)

