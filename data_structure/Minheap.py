class MinHeap:
    def __init__(self):
        self.heap = []

    # 获取父节点的索引
    def _parent(self, i):
        return (i - 1) // 2

    # 获取左子节点的索引
    def _left(self, i):
        return 2 * i + 1

    # 获取右子节点的索引
    def _right(self, i):
        return 2 * i + 2

    # 上浮操作（插入时使用）
    def _upheap(self, i):
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            # 交换当前节点和父节点
            self.heap[self._parent(i)], self.heap[i] = self.heap[i], self.heap[self._parent(i)]
            i = self._parent(i)

    # 下沉操作（删除堆顶元素时使用）
    def _downheap(self, i):
        n = len(self.heap)
        while self._left(i) < n:
            left = self._left(i)
            right = self._right(i)
            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != i:
                # 交换当前节点和最小子节点
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    # 插入元素
    def insert(self, val):
        self.heap.append(val)
        self._upheap(len(self.heap) - 1)

    # 删除并返回堆顶元素（最小元素）
    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("pop from empty heap")
        min_val = self.heap[0]
        # 将堆的最后一个元素移到堆顶
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._downheap(0)
        return min_val

    # 获取堆顶元素（最小元素）
    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    # 获取堆的大小
    def size(self):
        return len(self.heap)

    # 判断堆是否为空
    def is_empty(self):
        return len(self.heap) == 0

    # 打印堆
    def print_heap(self):
        print(self.heap)

# 测试代码
if __name__ == "__main__":
    min_heap = MinHeap()

    # 插入一些元素
    min_heap.insert(3)
    min_heap.insert(1)
    min_heap.insert(5)
    min_heap.insert(2)
    min_heap.insert(4)

    print("堆的元素：")
    min_heap.print_heap()  # 输出：[1, 2, 5, 3, 4]

    # 获取堆顶元素（最小元素）
    print("堆顶元素：", min_heap.peek())  # 输出：1

    # 弹出堆顶元素
    print("弹出的最小元素：", min_heap.pop())  # 输出：1
    min_heap.print_heap()  # 输出：[2, 3, 5, 4]

    print("堆的大小：", min_heap.size())  # 输出：4
