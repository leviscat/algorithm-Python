class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # B树的阶（最小度）
        self.leaf = leaf  # 该节点是否是叶子节点
        self.keys = []  # 存储节点的键值
        self.children = []  # 存储节点的子节点（只有内部节点才有子节点）


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, leaf=True)  # 初始化根节点
        self.t = t  # B树的阶（最小度）

    # 查找一个键
    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node, i
        if node.leaf:
            return None
        return self.search(node.children[i], key)

    # 插入键值到B树中
    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            # 如果根节点已满，需要分裂根节点
            new_node = BTreeNode(self.t, leaf=False)
            new_node.children.append(self.root)
            self.split(new_node, 0)
            self.root = new_node
        self.insert_non_full(self.root, key)

    # 在非满节点中插入键值
    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            # 如果是叶子节点，直接插入
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # 如果是内部节点，找到合适的子节点进行递归插入
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t - 1):
                # 如果子节点满了，先分裂子节点
                self.split(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    # 分裂节点
    def split(self, parent, index):
        node = parent.children[index]
        new_node = BTreeNode(self.t, leaf=node.leaf)
        mid_key = node.keys[self.t - 1]

        # 将node的后半部分键值移动到新节点
        new_node.keys = node.keys[self.t:]
        node.keys = node.keys[:self.t - 1]

        if not node.leaf:
            new_node.children = node.children[self.t:]
            node.children = node.children[:self.t]

        # 将中间的键值提升到父节点
        parent.keys.insert(index, mid_key)
        parent.children.insert(index + 1, new_node)

    # 删除键值
    def delete(self, key):
        self.delete_helper(self.root, key)
        if len(self.root.keys) == 0:
            # 如果根节点没有键了，更新根节点
            if len(self.root.children) > 0:
                self.root = self.root.children[0]

    # 删除操作的递归实现
    def delete_helper(self, node, key):
        idx = 0
        while idx < len(node.keys) and key > node.keys[idx]:
            idx += 1

        if idx < len(node.keys) and key == node.keys[idx]:
            # 删除键值
            if node.leaf:
                node.keys.pop(idx)
            else:
                self.delete_internal_node(node, idx)
        elif node.leaf:
            return
        else:
            self.delete_internal_node(node, idx)

    # 删除内部节点的键值
    def delete_internal_node(self, node, idx):
        if len(node.children[idx].keys) >= self.t:
            # 如果前一个子树有足够的键值，找到前驱并递归删除
            predecessor_key = self.get_predecessor(node, idx)
            node.keys[idx] = predecessor_key
            self.delete_helper(node.children[idx], predecessor_key)
        elif len(node.children[idx + 1].keys) >= self.t:
            # 如果后一个子树有足够的键值，找到后继并递归删除
            successor_key = self.get_successor(node, idx)
            node.keys[idx] = successor_key
            self.delete_helper(node.children[idx + 1], successor_key)
        else:
            # 如果两个子树都没有足够的键值，则合并
            self.merge(node, idx)
            self.delete_helper(node.children[idx], node.keys[idx])

    # 获取前驱节点（前一个子树的最大键）
    def get_predecessor(self, node, idx):
        current_node = node.children[idx]
        while not current_node.leaf:
            current_node = current_node.children[len(current_node.children) - 1]
        return current_node.keys[len(current_node.keys) - 1]

    # 获取后继节点（后一个子树的最小键）
    def get_successor(self, node, idx):
        current_node = node.children[idx + 1]
        while not current_node.leaf:
            current_node = current_node.children[0]
        return current_node.keys[0]

    # 合并节点
    def merge(self, parent, idx):
        left_child = parent.children[idx]
        right_child = parent.children[idx + 1]
        mid_key = parent.keys.pop(idx)

        # 将父节点的中间键移到合并后的子节点中
        left_child.keys.append(mid_key)
        left_child.keys.extend(right_child.keys)
        left_child.children.extend(right_child.children)

        parent.children.pop(idx + 1)
# 创建B树，阶为3
btree = BTree(3)

# 插入键值
keys = [10, 20, 5, 6, 12, 30, 7, 17]
for key in keys:
    btree.insert(key)

# 查找某个键值
result = btree.search(btree.root, 6)
if result:
    print(f"Found {result[0].keys[result[1]]} at position {result[1]}")
else:
    print("Not found")

# 删除某个键值
btree.delete(6)
result = btree.search(btree.root, 6)
if result:
    print(f"Found {result[0].keys[result[1]]} at position {result[1]}")
else:
    print("Not found")