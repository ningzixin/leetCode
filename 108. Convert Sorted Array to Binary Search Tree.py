# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class CopyNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.height = None
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        构造平衡二叉树
        """
    def SingleLeftRotation(self,A):
        B = A.left
        A.left = B.right
        B.right = A
        A.height = max(self.GetHeight(A.left),self.GetHeight(A.right))+1
        B.height = max(self.GetHeight(B.left),A.height) + 1

    def SingleRightRoattion(self,A):
        B = A.right
        A.right = B.left
        B.left = A
        A.height = max(self.GetHeight(A.left),self.GetHeight(A.right))+1
        B.height =  max(self.GetHeight(B.right),A.height) + 1

    def DoubleLeftRightRotation(self,A):
        A.left = self.SingleRightRotation(A.Left);
        return self.SingleLeftRotation(A)

    def DoubleRightLeftRotation(self,A):
        A.right = self.SingleLeftRotation(A.right)
        return self.SingleRightRoattion(A)

    def GetHeight(self,T):
        if T==None:
            return 0
        else:
            return int(T.height)
    def mymax(self,a,b):
        if(a>b):
            return a
        else:
            return b
    def Insert(self,T,x):
        if T == None:
            T = CopyNode(x)
            T.height = 0
        elif x < T.val:
            T.left =self.Insert(T.left,x)
            if self.GetHeight(T.left) - self.GetHeight(T.right) == 2:
                if  x<T.left.val:
                    T = self.SingleLeftRotation(T)
                else:
                    T = self.DoubleLeftRightRotation(T)
        elif x > T.val:
            if self.GetHeight(T.left) - self.GetHeight(T.right) == -2:
                if x < T.right.val:
                    T = self.SingleRightRoattion(T)
                else:
                    T = self.DoubleRightLeftRotation(T)
        T.height = self.mymax(self.GetHeight(T.left), self.GetHeight(T.right)) + 1;
        return T

ll =  [-10,-3,0,5,9]
for i in ll:
    Solution.Insert("",None,i)