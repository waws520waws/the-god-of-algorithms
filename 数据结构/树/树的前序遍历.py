# 前序遍历

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
# 前序中的序表示的是root的顺序，前序就是root在前边，先中，左，再右，深度优先搜索
def pre_order(root):
    if root:
        print(root.data,end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)


pre_order(e)