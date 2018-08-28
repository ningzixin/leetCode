# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        count = 0 #存储层级
        ll = [] #存储返回结果
        ll_now = [] #当前的节点
        ll_next = [] #接下来所有的节点
        if root!=None:
            ll_now.append(root)

        for node in ll_now:
            if (node.left != None):
              ll_next.append(node.left)
            if (node.right != None):
                ll_next.append(node.right)

        while(ll_now!=None and len(ll_now)!=0):
            count += 1
            ll_next.clear()
            ll_ave = []

            for node in ll_now:
                ll_ave.append(node.val)
                if(node.left != None):
                    ll_next.append(node.left)
                if(node.right != None):
                    ll_next.append(node.right)
            ll.append(ll_ave)
            ll_now.clear()
            for node in ll_next:
                ll_now.append(node)
        ll = ll[::-1]
        return ll
s = TreeNode(3)
print(Solution.levelOrderBottom("",s))
