# 后序遍历

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
# 后序中的序表示的是root的顺序，前序就是root在后边，先左，右，最后中，深度优先搜索
def after_order(root):
    if root:
        after_order(root.lchild)
        after_order(root.rchild)
        print(root.data, end=",")

after_order(e)