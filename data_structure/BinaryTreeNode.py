class BinaryTreeNode:
    def __init__(self, value):
        self.value = value  # 存储节点值
        self.left = None  # 左子节点
        self.right = None  # 右子节点

# 创建节点
root = BinaryTreeNode('A')
node_b = BinaryTreeNode('B')
node_c = BinaryTreeNode('C')
node_d = BinaryTreeNode('D')
node_e = BinaryTreeNode('E')
node_f = BinaryTreeNode('F')

# 构建树的结构
root.left = node_b
root.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.right = node_f

# 访问根节点及其子节点
print(root.value)  # A
print(root.left.value)  # B
