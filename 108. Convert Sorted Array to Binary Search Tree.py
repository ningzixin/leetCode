# Definition for a binary tree node.
from queue import Queue
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

def sortedArrayToBST(nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        构造平衡二叉树
        """
def SingleLeftRotation(A):
        B = A.left
        A.left = B.right
        B.right = A
        A.height = max(GetHeight(A.left),GetHeight(A.right))+1
        B.height = max(GetHeight(B.left),A.height) + 1
        return B

def SingleRightRoattion(A):
        B = A.right
        A.right = B.left
        B.left = A
        A.height = max(GetHeight(A.left),GetHeight(A.right))+1
        B.height =  max(GetHeight(B.right),A.height) + 1
        return B

def DoubleLeftRightRotation(A):
        A.left = SingleRightRoattion(A.Left)
        return SingleLeftRotation(A)

def DoubleRightLeftRotation(A):
        A.right = SingleLeftRotation(A.right)
        return SingleRightRoattion(A)

def GetHeight(T):
        if T==None:
            return 0
        else:
            return int(T.height)
def mymax(a,b):
        if(a>b):
            return a
        else:
            return b
def Insert(T,x):
        if T == None:
            T = CopyNode(x)
            T.height = 0
        elif x < T.val:
            T.left =Insert(T.left,x)
            if GetHeight(T.left) - GetHeight(T.right) == 2:
                if  x > T.left.val:
                    T = SingleLeftRotation(T)
                else:
                    T = DoubleLeftRightRotation(T)
        elif x > T.val:
            T.right = Insert(T.right, x)
            if GetHeight(T.left) - GetHeight(T.right) == -2:
                if x > T.right.val:
                    T = SingleRightRoattion(T)
                else:
                    T = DoubleRightLeftRotation(T)
        T.height = mymax(GetHeight(T.left), GetHeight(T.right)) + 1
        return T

def level(T):
    q = []
    q.append(T)
    while len(q) !=0:
        T = q[0]
        q.pop(0)
        print(T.val)
        if T.left!=None:
            q.append(T.left)
        if T.right!=None:
            q.append(T.right)


ll =  [-10,-3,0,5,9]
T = None
for i in ll:
    T = Insert(T,i)
level(T)

#高度平衡的二叉搜索树
