class Node:
    def __init__(self, data):
        self.data = data
        self.color = 'R'  # 新节点默认为红色
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)  # 代表空节点，黑色
        self.TNULL.color = 'B'
        self.root = self.TNULL
        #TNULL没有定义为什么不会报错呢？因为TNULL是在__init__方法中定义的，所以不会报错
        #为什么在__init__方法中定义的变量不会报错呢？因为在python中，变量是动态类型的，所以不会报错
        #什么是动态类型呢？动态类型就是变量的类型是在运行时确定的，而不是在编译时确定的
    # 左旋转操作
    def left_rotate(self, x):
        y = x.right
        x.right = y.left  #修改了x的右子树
        if y.left != self.TNULL:
            y.left.parent = x#修改了y的左子树的父节点
            #将y的左子树和x连接起来
        y.parent = x.parent  #修改了y的父节点
        if x.parent == None: #修改了x的父节点
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            #将y和x之前的父节点连接起来
        y.left = x  #修改了y的左子树
        x.parent = y #修改了x的父节点
         #将x和y连接起来
    # 右旋转操作
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # 插入修复函数，保证红黑树的性质
    def insert_fix(self, k):
        #k是新插入的节点，整个循环的目的是为了保证红黑树的性质
        # 红黑树需要满足以下性质：
        #
        # 每个节点要么是红色，要么是黑色。
        # 根节点必须是黑色。
        # 红色节点的子节点必须是黑色（红色节点不能有红色子节点）。
        # 从任意节点到其叶子节点的每条路径都包含相同数量的黑色节点。
        while k.parent.color == 'R':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right  # 叔叔节点
                if u.color == 'R':
                    # Case 1: 叔叔是红色
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                    #叔叔和父节点都是红色，树的结构已经平衡（左右子树高度一致）。但是根节点是红色，所以需要将根节点改为黑色
                else:
                    if k == k.parent.right:
                        # Case 2: 叔叔是黑色，且当前节点在右子树
                        k = k.parent
                        self.left_rotate(k)
                        #通过左旋，可以将调整到左子树，使树的结构便于后续修复。
                    # Case 3: 叔叔是黑色，且当前节点在左子树
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    #通过右旋，可以将左子树重新平衡
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.left_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'B'

    # 插入操作
    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'R'

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        #不断遍历找到node的父节点
        node.parent = y
        if y is None:  #为什么y会是None呢？因为在上面的while循环中，x是self.root，所以y就是None,其实就是没有进入while循环的时候
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 'B'
            return

        if node.parent.parent is None:
            return
#如果新节点的父节点没有祖父节点，那么直接返回，修复过程就是为了保证红黑树的性质
# 1.每个节点要么是红色要么是黑色 2.根节点是黑色 3.每个叶子节点是黑色 4.如果一个节点是红色，那么它的子节点都是黑色 5.从任意节点到叶子节点的路径上包含相同数量的黑色节点
        self.insert_fix(node)

    # 中序遍历
    def inorder(self, root):
        if root != self.TNULL:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
# 测试红黑树的插入
rbt = RedBlackTree()
rbt.insert(20)
rbt.insert(15)
rbt.insert(25)
rbt.insert(10)
rbt.insert(5)
rbt.insert(1)

rbt.inorder(rbt.root)
