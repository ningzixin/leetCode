# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if (self.preorderleft(root, "") == self.preorderright(root, "")):
            return True
        return False

    def preorderleft(self, root, string):
        if (root == None):
            return string + "_"
        return str(root.val) + self.preorderleft(root.left, string) + self.preorderleft(root.right, string)
    def preorderright(self, root, string):
        if (root == None):
            return string + "_"
        return str(root.val) + self.preorderright(root.right, string) + self.preorderright(root.left, string)