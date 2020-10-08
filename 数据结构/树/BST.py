class BiTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST(object):
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def query(self,node,val):
        if not node:   # 其实这个部分是判断查询是否到了空节点，到了，还没有查到，说明没有符合条件的数据
            return None
        elif val < node.data:
            return self.query(node.lchild, val)
        elif val > node.data:
            return self.query(node.rchild, val)
        else:
            return node

    def query_no_rec(self,val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        else:
            return None

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    # 删除的节点是叶子，
    def __remove_node_1(self,node):
        if not node.parent:
            self.root = None
        # 如果是父亲的左孩子
        if node == node.parent.lchild:
            node.parent.lchild = None
        # 如果是父亲的右孩子
        else:
            node.parent.rchild = None

    # 删除的节点只有一个左孩子
    def __remove_node_21(self, node):
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        # 如果是父亲的左孩子
        if node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        # 如果是父亲的右孩子
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    # 删除的节点只有一个右孩子
    def __remove_node_22(self, node):
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        # 如果是父亲的左孩子
        if node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        # 如果是父亲的右孩子
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self,val):
        if self.root:  # 不是空树
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            elif not node.rchild:   # 只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild:   # 只有一个右孩子
                self.__remove_node_22(node)
            else:    # 左右孩子都存在
                # 查找左子树的最小值节点
                min_node= node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                # 数值作替换，相当于将节点移动上去了
                node.data = min_node.data
                # 然后将右子树连接到他的父节点上
                if not min_node.rchild:
                    self.__remove_node_1(min_node)
                else:
                    self.__remove_node_22(min_node)




    def mid_order(self, root):
        if root:
            self.mid_order(root.lchild)
            print(root.data, end=",")
            self.mid_order(root.rchild)

    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def after_order(self, root):
        if root:
            self.after_order(root.lchild)
            self.after_order(root.rchild)
            print(root.data, end=",")


if __name__ == '__main__':
    tree = BST([2, 3, 54, 6, 11, 4, 7, 15, 3, 78, 21, 79 ])
    tree.pre_order(tree.root)
    print("")
    # 我们发现中序的已经按照从小到大的顺序进行了排列
    tree.mid_order(tree.root)
    print("")
    tree.after_order(tree.root)

    """
    2,3,54,6,4,11,7,15,21,78,79,
    2,3,4,6,7,11,15,21,54,78,79,
    4,7,21,15,11,6,79,78,54,3,2,
    """
    print("")
    result = tree.query(tree.root,54)
    if result:
        print(result.data)
    else:
        print(result)
    "----------------------------------------------"
    result = tree.query_no_rec(54)
    if result:
        print(result.data)
    else:
        print(result)

    "----------------------------------------------"
    tree.delete(54)
    tree.mid_order(tree.root)