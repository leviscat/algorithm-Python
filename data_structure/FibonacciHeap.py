import math


class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key  # 存储的键值
        self.degree = 0  # 该节点的度（子节点数）
        self.parent = None  # 父节点
        self.child = None  # 子节点
        self.mark = False  # 标记字段
        self.next = None  # 指向下一个节点的指针
        self.prev = None  # 指向前一个节点的指针


class FibonacciHeap:
    def __init__(self):
        self.min = None  # 最小值的指针
        self.total_nodes = 0  # 堆中节点的总数

    def insert(self, key):
        # 创建新的节点并插入到根链表
        new_node = FibonacciHeapNode(key)
        if self.min is None:
            self.min = new_node
            new_node.next = new_node
            new_node.prev = new_node
            #如果最小值为空，说明堆中没有元素，将新节点作为最小值，他的next和prev都指向自己
        else:
            # 插入到根链表
            #不为空将新节点插入到根链表中为什么要用min.prev呢？因为min是最小值，min.prev是最大值，将新节点插入到最大值的前面
            self._link_nodes(self.min.prev, new_node)
            if key < self.min.key:
                self.min = new_node
        self.total_nodes += 1

    def _link_nodes(self, node1, node2):
        node1.next.prev = node2
        node2.next = node1.next
        node1.next = node2
        node2.prev = node1


    def remove_min(self):
        if self.min is None:
            return None

        min_node = self.min
        if min_node.child is not None:
            # 将子节点添加到根链表
            child = min_node.child
            while True:
                next_child = child.next
                child.prev = min_node.prev
                min_node.prev.next = child
                child.next = self.min
                self.min.prev = child
                child.parent = None
                if next_child == min_node.child:
                    break
                child = next_child

        # 删除最小节点
        min_node.prev.next = min_node.next
        min_node.next.prev = min_node.prev
        if min_node == min_node.next:
            self.min = None
        else:
            self.min = min_node.next
            self._consolidate()

        self.total_nodes -= 1
        return min_node.key

    def _consolidate(self):
        # 通过合并根节点来维持堆的结构
        max_degree = int(math.log(self.total_nodes) / math.log(2)) + 1
        degree_table = [None] * (max_degree + 1)

        current = self.min
        nodes = []
        while True:
            nodes.append(current)
            current = current.next
            if current == self.min:
                break

        for node in nodes:
            degree = node.degree
            while degree_table[degree] is not None:
                other_node = degree_table[degree]
                if other_node.key < node.key:
                    node, other_node = other_node, node
                self._link_nodes(node, other_node)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = node

        self.min = None
        for node in degree_table:
            if node is not None:
                if self.min is None or node.key < self.min.key:
                    self.min = node

    def get_min(self):
        return self.min.key if self.min is not None else None


# 示例
f_heap = FibonacciHeap()
f_heap.insert(3)
f_heap.insert(2)
f_heap.insert(8)
f_heap.insert(5)
print("Min:", f_heap.get_min())  # 输出最小值

print("Remove Min:", f_heap.remove_min())  # 移除最小值
print("Min after remove:", f_heap.get_min())  # 输出新的最小值
