class CopyNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def isBalanced( root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    getHight(root)
    check(root)
    return True


def getHight(root):
    if root.left != None:
        getHight(root.left)
    if root.right != None:
        getHight(root.right)
    if root.left == None and root.right == None:
        root.hight = 0
    if root.left == None and root.right != None:
        root.hight = root.right.hight + 1
    if root.left != None and root.right == None:
        root.hight = root.left.hight + 1
    if root.left != None and root.right != None:
        root.hight = max(root.left.hight, root.right.hight) + 1


def check( root):
    if root.right != None and root.left != None:
        if root.left.hight - root.right.hight == 2 or root.left.hight - root.right.hight == -2:
            return False
    if root.right !=None and root.left==None:
        if root.hight==2:
            return False
    if root.left!=None and root.right == None:
        if root.hight == 2:
            return False
    if root.left != None:
        return check(root.left)
    if root.right != None:
        return check(root.right)
    return True

def level(T):
    q = []
    q.append(T)
    while len(q) != 0:
        T = q[0]
        q.pop(0)
        if T.right != None and T.left != None:
            if T.left.hight - T.right.hight == 2 or T.left.hight - T.right.hight == -2:
                return False
        if T.right != None and T.left == None:
            if T.hight == 2:
                return False
        if T.left != None and T.right == None:
            if T.hight == 2:
                return False
        if T.left != None:
            q.append(T.left)
        if T.right != None:
            q.append(T.right)
    return True
flag = 1
T = CopyNode(1)
T.left =CopyNode(2)
T.right = CopyNode(3)
T.left.left = CopyNode(4)
T.left.right = CopyNode(5)
T.right.right = CopyNode(6)
T.left.left.left = CopyNode(7)
T.right.right.right = CopyNode(8)
getHight(T)
print(level(T))
print(check(T))