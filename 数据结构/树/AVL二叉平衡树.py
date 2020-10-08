from BST import  BiTreeNode,BST

class AVLNode(BiTreeNode):
    def __init__(self,data):
        BiTreeNode.__init__(self,data)
        self.bf = 0

class AVLTree(BST):
    def __init__(self,li = None):
        BST.__init__(self,li)

    # 四种旋转都是最终要得到变化之后的树的根(所以最终的返回都是调整后的树的root)
    def rotate_left(self,p,c):
        # 插入没有问题，但是删除的时候会出现问题
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self,p,c):
        # 插入没有问题，但是删除的时候会出现问题
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c
        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self,p,c):
        # 插入没有问题，但是删除的时候会出现问题
        g = c.lchild
        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        if g.bf > 0:
            # 插入到s3
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            # 插入到s2
            p.bf = 0
            c.bf = 1
        else:
            # 插入到g
            p.bf = 0
            c.bf = 0
        g.bf =0
        return g

    def rotate_left_right(self,p,c):
        # 插入没有问题，但是删除的时候会出现问题
        g = c.rchild
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        if g.bf > 0:
            # 插入到s3
            p.bf = 0
            c.bf = -1
        elif g.bf < 0:
            # 插入到s2
            p.bf = 1
            c.bf = 0
        else:
            # 插入到g
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g


    def insert_no_rec(self, val):
        # 1.和BST一样，插入
        p = self.root
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild   # node存储的就是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild   # node存储的就是插入的节点
                    break
            else:
                return

        # 2.更新balance factor
        while node.parent: # 保证node.parent不空
            if node.parent.lchild == node:   # 假设传递是从左子树来的，左子树更沉了
                # 更新node.parent的bf -=1
                if node.parent.bf < 0:  # 说明node.parent.bf=-1 更新之后变成了-2
                    # 看node的那边沉，如果是左边比较沉，就是右旋
                    #                 如果是右边比较沉，就是先左旋后右旋
                    g = node.parent.parent    #为了连接旋转之后的子树
                    x = node.parent   # 旋转之前的父节点
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent,node)
                    else:
                        n = self.rotate_right(node.parent,node)
                    """
                    TODO 记得将g和n连接起来
                    """
                elif node.parent.bf > 0:# 说明node.parent.bf=1 更新之后变成了0
                    # 不需要旋转
                    node.parent.bf = 0
                    break
                else:                 # 说明node.parent.bf=0 更新之后变成了-1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:# 假设传递是从右子树来的，右子树更沉了
                # 更新node.parent的bf +=1
                if node.parent.bf > 0:  # 说明node.parent.bf=1 更新之后变成了2
                    # 看node的那边沉，如果是左边比较沉，就是先右旋后左旋
                    #                 如果是右边比较沉，就是左旋
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent  # 旋转之前的父节点
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                    """
                    TODO 记得将g和n连接起来
                    """
                elif node.parent.bf < 0:  # 说明node.parent.bf=-1 更新之后变成了0
                    # 不需要旋转
                    node.parent.bf = 0
                    break
                else:  # 说明node.parent.bf=0 更新之后变成了1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 连接旋转后的子树
            n.parent = g
            if g:
                if x == g.lchild:  # 是要看原来的node是怎样连接的，原来是g的左子树，n连在g的左子树上，否则是右边
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break


tree = AVLTree([2, 3, 54, 6, 11, 4, 7, 15, 3, 78, 21, 79 ])
# 我们发现中序的已经按照从小到大的顺序进行了排列
tree.mid_order(tree.root)
