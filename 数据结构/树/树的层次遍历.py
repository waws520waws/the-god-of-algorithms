# 层次遍历

class BiTreeNode(object):
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e


# 层次遍历是将树从上到下从左到右的不断输出,广度优先搜索
def floor_order(root):
    li = []
    li.append(root)
    while len(li):
        root = li.pop(0)
        if root:
            print(root.data, end=",")
            li.append(root.lchild)
            li.append(root.rchild)


floor_order(e)