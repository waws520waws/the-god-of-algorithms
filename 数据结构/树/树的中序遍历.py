# 中序遍历

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


# 中序中的序表示的是root的顺序，中序就是root在中间，先左，中，再右，深度优先搜索
def mid_order(root):
    if root:
        mid_order(root.lchild)
        print(root.data, end=",")
        mid_order(root.rchild)


mid_order(e)