class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if not node:
        return 0
    return node.window_height

def getBlance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    print("rotate right on node",y.data)
    x = y.left
    T2 = x.right
    x.right = yy.left =T2
    y.height = 1+ max(getHeight(y.left),grtHeight(y.right))
    x.height = 1 + max(getHeight(x.left),getHeight(x.right))
    return x