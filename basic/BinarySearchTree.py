import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # 插入节点到BST中
    def insert(self, value):
        if not self.root:#这个语法是python的特色，如果self.root是None，那么not self.root就是True
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)
#insert和_insert的区别是什么呢？insert是对外的接口，_insert是对内的接口  对内接口相当于java的private方法 对外接口相当于public方法
    # 辅助函数，递归插入
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    # 中序遍历树并返回值
    def inorder(self):
        return self._inorder(self.root)
#为什么上述调用_inorder方法时，传入的参数是一个，但是在_inorder方法中，传入的参数是两个呢？
#因为在调用inorder方法时，只传入了一个参数，但是在_inorder方法中，是递归调用的，所以在递归调用的时候，需要传入两个参数
    #但是在java中必须传入两个参数，为什么呢？因为java中没有默认参数，所以必须传入两个参数
    #什么是默认参数呢？默认参数就是在定义方法的时候，给参数赋一个默认值，如果调用方法时没有传入参数，那么就会使用默认值
    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

# 随机生成节点值
def generate_random_bst(size, lower_bound, upper_bound):
    bst = BST()
    values = random.sample(range(lower_bound, upper_bound), size)  # 随机生成不重复的整数
    for value in values:
        bst.insert(value)
    return bst

# 测试
size = 10  # 生成10个随机节点
lower_bound = 1
upper_bound = 100
random_bst = generate_random_bst(size, lower_bound, upper_bound)
# 打印中序遍历结果，应该是一个有序的列表
print("中序遍历结果:", random_bst.inorder())
